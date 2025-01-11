# api_final
api_yatube - это продукт REST API для блог-платформы Yatube, который позволяет просматривать посты и комментарии к ним, а также предоставляет возможность авторам изменять и удалять их при необходимости. Проект также предусматривает наличие групп, которые также можно просматривать.

Как запустить проект:

1. Клонирование репозитория:

git clone https://github.com/AlisaUrikh/api_final_yatube.git

2. Cоздание и активация виртуального окружения:

cd api_final_yatube
python -m venv venv
source venv/Scripts/activate 

3. Установка зависимостей:

pip install -r requirements.txt

4. Выполнение миграций:

python manage.py migrate

5. Запуск проекта:

python manage.py runserver

Примеры запросов:
GET http://127.0.0.1:8000/api/v1/follow/ 
При успешном запросе в ответ пользователь получит список своих подписок в формате JSON:
{
"user": "string",
"following": "string"
}
POST http://127.0.0.1:8000/api/v1/posts/ - создание публикации
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ - обновление комментария

В ответ вернется