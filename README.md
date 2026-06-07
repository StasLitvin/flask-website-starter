<<<<<<< HEAD
# flask-website-starter
=======
# flask — учебный веб-сайт на Flask

Простой многостраничный сайт на Flask с регистрацией пользователей и хранением данных в SQLite через SQLAlchemy. Похоже на учебный/стартовый проект.

## Структура проекта

```
flask/
├── app.py                 # приложение Flask, модель User, маршруты
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── services.html
    ├── contact.html
    └── register.html
```

## Возможности

- Главная, «О нас», «Услуги», «Контакты», страница регистрации.
- Модель `User` (username, email, password, дата регистрации) в SQLite (`site.db`).
- Flash-сообщения, шаблонизация на Jinja2 (наследование от `base.html`).

## Технологии

Flask 2.3, Flask-SQLAlchemy 3.0, SQLite.

## Запуск

```bash
pip install -r requirements.txt
python app.py
```

Сайт будет доступен на `http://127.0.0.1:5000/`.

## ⚠️ Замечания

- `SECRET_KEY` захардкожен значением-заглушкой — для реального использования замените на случайный и храните в окружении.
- Пароли в модели хранятся как обычная строка — для продакшена нужно хэширование (например, `flask-bcrypt`, как сделано в `projects2/app.py`).
>>>>>>> 903dc71 (Add files)
