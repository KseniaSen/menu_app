# API для вывода меню

Для реализации данного проекта были использованы технологии Python 3 и фреймворк Django.

## Требования к окружению

- Python 3.7 и выше
- Установленные библиотеки из requirements.txt

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.7 и выше.
2. Клонируйте репозиторий, создайте виртуальное окружение.
3. Установите необходимые библиотеки: pip install -r requirements.txt
4. Создайте базу данных:
- создайте миграции: cd ../menu_project && python manage.py make migrations
- применените миграции: python manage.py migrate
5. Создайте суперпользователя: python manage.py createsuperuser
6. Запустите сервер: python manage.py runserver


