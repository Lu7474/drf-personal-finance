## Finance API — Sprint 1

### Описание

Backend REST API сервиса учета личных финансов.
Спринт 1 содержит базовый скелет проекта без бизнес-логики и авторизации.

Цель спринта — подготовить чистую архитектурную основу для дальнейшей разработки.

---

## Стек

* Python 3.11
* Django
* Django REST Framework
* PostgreSQL
* dotenv

---

## Что реализовано в Спринте 1

* инициализирован Django проект
* разделение настроек (base / local)
* подключен Django REST Framework
* подключена PostgreSQL
* конфигурация через env-переменные
* базовая структура приложений
* healthcheck эндпоинт

---

## Структура проекта

```
finance_api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── users/
│   ├── accounts/
│   ├── categories/
│   ├── transactions/
│   └── reports/
│
├── manage.py
└── README.md
```

---

## Переменные окружения

Создать файл `.env` в корне проекта:

```
DEBUG=True
SECRET_KEY=unsafe-secret
DB_NAME=finance
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

---

## Запуск проекта

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## Healthcheck

```
GET /health/
```

Ответ:

```json
{
  "status": "ok"
}
```

Используется для проверки доступности сервиса.

---

## Примечания

* авторизация и бизнес-логика будут добавлены в следующих спринтах
* проект пока работает в режиме публичного API

---

## Планы на следующий спринт

* кастомная модель пользователя
* JWT авторизация
* защита API эндпоинтов