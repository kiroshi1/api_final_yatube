Описание: 
Этот проект позволяет пользователям получать доступ через API к постам, группам, подписчикам, комментариям и прочему.
Создавать, удалять объекты, редактировать их по своему усмотрению
Установка:
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver
