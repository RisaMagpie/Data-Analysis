from elasticsearch import Elasticsearch
import requests
from  elasticsearch.helpers import scan as scan
es = Elasticsearch([{"host": "localhost", "port": 9200}])

import pandas as pd


from .getTestsSeqPos import getListsOfProblemsSequential
gradedProblemsSeqArray, ungradedProblemsSeqArray, finalExamSeq=getListsOfProblemsSequential() 
gradedProblemsSeqArray=pd.DataFrame(gradedProblemsSeqArray, columns = ['seq','pos','problem_id'])
ungradedProblemsSeqArray=pd.DataFrame(ungradedProblemsSeqArray, columns = ['seq','pos','problem_id'])

body={
    "_source": [
        "context.user_id",
        "context.course_id",
        "referer",
        "time",
        "str_event",
        "event_type"
    ],
    "query": {
        "bool":{
            "should":[                
                {"match_phrase":{
                    "event_type": "seq_next"
                }},
                {"match_phrase":{
                    "event_type": "seq_prev"
                }},
                {"wildcard":{
                    "event_type": "*goto_position"
                }}           
            ]         
        }
    }
}

def ret():
    for hit in scan(es,
         index="online_courses_full", 
         query=body
        ):        
        if hit.get("_source").get("str_event") :
            event_type=hit.get("_source").get("event_type")
            if event_type=="seq_prev" or event_type=="seq_next":
                tmpString=hit.get("_source").get("str_event")
                sequence=tmpString.split("sequential+block@")[-1].split("\"")[0]
                position=tmpString.split("\"new\": ")[-1].split(",")[0]
            else:
                tmpString=hit.get("_source").get("event_type")
                sequence=tmpString.split("sequential+block@")[-1].split("/")[0]
                tmpString=hit.get("_source").get("str_event")
                position=tmpString.split("\"position\": [\"")[-1].split("\"]")[0]
            problem_id=''

            if int(position) in list(gradedProblemsSeqArray.loc[gradedProblemsSeqArray['seq'] == sequence]['pos']):
                problemFlag='graded'
                tmpdf=gradedProblemsSeqArray.loc[gradedProblemsSeqArray['seq'] == sequence]
                tmpdf=tmpdf.loc[tmpdf['pos'] == int(position)]
                problem_id=list(tmpdf['problem_id'])[0]
            elif int(position) in list(ungradedProblemsSeqArray.loc[ungradedProblemsSeqArray['seq'] == sequence]['pos']):
                problemFlag='ungraded'
                tmpdf=ungradedProblemsSeqArray.loc[ungradedProblemsSeqArray['seq'] == sequence]
                tmpdf=tmpdf.loc[tmpdf['pos'] == int(position)]
                problem_id=list(tmpdf['problem_id'])[0]
            elif (sequence in finalExamSeq) and (position in finalExamSeq):
                problemFlag='final'
            else:
                problemFlag=False
                
            if problemFlag:
                yield {                    
                    "user_id":hit.get("_source").get("context").get("user_id"),
                    "course_id":hit.get("_source").get("context").get("course_id"),
                    "time":hit.get("_source").get("time"),
                    "theme_id":hit.get("_source").get("referer").split('courseware/')[-1].split('/')[1],
                    #"sequence":sequence,
                    #"position":position,
                    "problem_type":problemFlag,
                    "problem_id":problem_id
                }