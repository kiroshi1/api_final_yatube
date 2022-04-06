# Yatube API

### Описание
Этот проект позволяет пользователям получать доступ через API к постам, группам, подписчикам, комментариям и прочему.
Создавать, удалять объекты, редактировать их по своему усмотрению
### Технологии
Python 3.7
Django 2.2.16

### Запуск проекта локально
- Клонировать репозиторий и перейти в него в командной строке
```
git clone https://github.com/kiroshi1/api_final_yatube.git
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
python -m venv env
venv/scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```
## Можно пользоваться по адресу 127.0.0.1


### Примеры запросов:
GET api/v1/posts/
Возвращает список всех постов.

[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
  }
]

POST api/v1/posts/
Создаёт пост, если вы в теле запроса передаёте переменную "text": "string",
возвращает созданный пост, где в кач-ве автора указан юзер, отправивший запрос.

"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0

### Разработчик
Denis Razgonyaev