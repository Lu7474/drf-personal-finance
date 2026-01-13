# Finance API

## Описание проекта

Finance API — backend REST API для сервиса учета личных финансов.
Проект разрабатывается по спринтам с постепенным наращиванием функциональности: от базовой архитектуры до полноценной системы учета доходов, расходов и отчетов.

Основной фокус:

* чистая архитектура
* REST API
* масштабируемость
* готовность к продакшену

Проект пишется на Django + Django REST Framework.

---

## Спринты

### Sprint 1 — Базовая архитектура

Подготовка каркаса проекта без бизнес-логики и авторизации.

* инициализация Django-проекта
* настройка окружения
* подключение DRF и базы данных
* healthcheck эндпоинт

---

### Sprint 2 — Users & Authentication

Реализация системы пользователей и аутентификации.

* кастомная модель пользователя
* регистрация
* JWT-аутентификация
* базовые тесты

---

## Стек

* Python 3.14
* Django
* Django REST Framework
* PostgreSQL
* dotenv
* SimpleJWT

---

## Установка и запуск

### Переменные окружения

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

### Запуск проекта

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## Структура проекта

```
FINA_API/
├── core/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── README.md
└── requirements.txt
```

---

## Sprint 1 — Реализовано

* инициализирован Django проект
* подключен Django REST Framework
* подключена PostgreSQL
* конфигурация через env-переменные
* базовая структура приложений
* healthcheck эндпоинт

### Healthcheck

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

## Sprint 2 — Users & Authentication

### Пользователи

* кастомная модель пользователя `CustomUser`
* логин по email
* подключён `AUTH_USER_MODEL`
* корректная работа миграций с кастомным пользователем

### Регистрация

* endpoint регистрации пользователя
* реализация через `CreateAPIView`
* используется `ModelSerializer`
* пароль хешируется через `create_user`
* пароль не возвращается в response (`write_only`)

### Валидации

* проверка уникальности email на уровне сериализатора
* валидация пароля (минимальная длина)
* проверка обязательных полей

### Аутентификация

* JWT-аутентификация через `djangorestframework-simplejwt`
* endpoint получения access / refresh токенов
* endpoint обновления access токена

### Тестирование

* добавлены тесты на регистрацию пользователя
* проверяется:

  * успешная регистрация
  * невозможность регистрации с существующим email
  * корректный формат ответа
  * отсутствие пароля в response

---

## API Endpoints

### Регистрация

```
POST /api/users/register/
```

**Request**

```json
{
  "email": "user@example.com",
  "username": "user",
  "password": "strongpassword"
}
```

**Response (201 Created)**

```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "user"
}
```

---

### Логин (JWT)

```
POST /api/users/login/
```

```json
{
  "access": "...",
  "refresh": "..."
}
```

---

### Обновление токена

```
POST /api/users/token/refresh/
```

---

## Архитектурные решения

* используется `AbstractUser` для минимальной кастомизации
* email выбран основным идентификатором пользователя
* логика создания пользователя вынесена в сериализатор
* view остаются тонкими, без бизнес-логики
* JWT используется как stateless-аутентификация для API

---

## Следующий шаг

Sprint 3:

* защищённые эндпоинты
* permissions и разграничение доступа
* бизнес-сущности (счета, категории, транзакции)
* привязка данных к пользователю

