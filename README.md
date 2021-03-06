# Data-Analysis
This repo was created for writing a diploma.

Данный проект является аккумулятором кода и статей для написания ВКР на тему анализа данных онлайн курсов (с привязкой к приложению анализа для построения модели адаптивного обучения).
В рамках осенней практики велась работа в составе команды над [проектом анализу данных в рамках задачи от ЦРЭОР](https://github.com/SpbSUPractiseTeam). Цель проекта – создать платформу для осуществления анализа данных онлайн курсов загружаемых пользователями логов.
В рамках ВКР был проведен анализ данных для построения рекомендаций для студентов и методистов. Эти рекомендации должны помочь персонализировать обучение слушателей в рамках онлайн курсов. На основании сформированных моделей слушатели разделяются на группы по уровню активности и стилю обучения, а также предлагаются методы рекомендации последовательности контента и рекомендации материалов для слушаетелей, которые плохо справились с какими-либо заданиями. В этом репозитории находится код исследования, описанного в ВКР. В данный репозиторий не были загружены данные, на основании которых производился анализ.

**Язык программирования**: **python** в пакете анализа данных **Anaconda**

**Представление данных логов**: формат: **JSON**, описание событий: [wiki](https://github.com/RisaMagpie/Data-Analysis/wiki/%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F), структура курса - набор файлов формата xml.

## Проект команды по анализу данных в рамках задачи от ЦРЭОР [:page_facing_up:](https://github.com/SpbSUPractiseTeam)
Процесс: методист загружает логи, на основании которых система проиводит анализ и выводит результат анализа.

### В этом проекте осуществляется анализ данных:
---
***Раздел видео:***
Анализ производится на основе событий видео.

- Средний процент просмотра видео для каждого видео
- Вывод диаграммы просмотра видео: количество просмотров каждого момента видео для каждого пользователя (интересуют моменты, которые просматривались несколько раз)
- Процент пользователей, просмотревших видео
---
***Раздел тесты:***
Анализ производится на основе событий контрольных тестов.

- Подсчет среднего балла участников курсов в каждом тесте
- Подсчет процента правильных ответов на каждый вопрос
---

## ВКР
Данные, полученные с платформы онлайн образования, загружаются в индекс Elasticsearch. Из xml файлов структуры курса извлекается информация о страницах, содержащих задания, для того, чтобы в дальнейшем вычислить время, потраченное пользователями на решение заданий.
Далее на основании файлов логов формируются модели пользователей, после чего производятся манипуляции над моделями, описанные в тексте ВКР.

