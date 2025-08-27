# Создание виртуального окружения 
1. Создать рабочую дирректорию
2. Перейти в созданную дирректорию через cmd или bash
3. Выполнить команду 'python -m venv env'
4. Перейти в папку './проект/env/Scripts' и выпонить команду ('ativate' в cmd  или 'sourse activate' в bash)
5. Вернуться на уровень проекта

# Создание Django проекта
1. Выполнить команду 'pip instal django'
2. Выполнить команду  'django-admin startproject имя проекта'
3. После выполнения команды из пункта 2, в папке с проектом будет создана папка, перейти в нее и выполнить команду ('manage.py runserver' в cmd   или   'python manage.py runserver' в bash)






# Добавление и запись нового файла: 
- git add .  (или git add название файла с разширением)
- git commit -m "описание файла или изменений"
- git push

# Создание виртуального окружения
- python -m venv env
- venv — имя папки, куда будут установлены файлы окружения. Можно назвать по другому

# Активировация виртуального окружение 
- source env/Scripts/activate

# Установка Django
- pip install django

# Скачивание репозитория
- git init
- git add remote add origin https://github.com/kunvitch111-png/new.git
- git pull origin master

# Открытие проекта с другого ПК
1. Клонировать проект с GitHub 
- git clone https://github.com/kunvitch111-png/new.git
- cd new
2. Создать виртуальное окружение
- python -m venv env
3. Активировать окружение
- source env/Scripts/activate
4. Установить зависимости requirements.txt
- pip install -r requirements.txt
5. Перейти в папку с проектом (c manage.py), применить миграции, запустить сервер
- cd newPro
- python manage.py migrate
- python manage.py runserver
