# RecipeBook

A Django REST API for managing recipes with token-based authentication. Each recipe includes a title, description, creation date, and author information.

## Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)

## Setup Instructions

### 1. Create and Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run Database Migrations

```powershell
python manage.py migrate
```

### 3. Create an Admin User (Optional)

```powershell
python manage.py createsuperuser
```

## Running the Application

Start the development server:

```powershell
python manage.py runserver
```

The application will be available at:

- **API Endpoint:** `http://127.0.0.1:8000/api/recipes-list/`
- **Admin Dashboard:** `http://127.0.0.1:8000/admin/`

## Authentication

All API endpoints require token-based authentication. Follow these steps to create and use a token:

### Generating a Token

1. Open the Django shell:

```powershell
python manage.py shell
```

2. Create a token for your user:

```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username="YOUR_USERNAME")
token, created = Token.objects.get_or_create(user=user)
print(token.key)
```

### Using the Token

Include the token in the `Authorization` header for all API requests:

```text
Authorization: Token YOUR_TOKEN_KEY
```

## API Endpoints

### Base URL

```text
http://127.0.0.1:8000/api/recipes-list/
```

### Available Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/recipes-list/` | Retrieve all recipes |
| `POST` | `/api/recipes-list/` | Create a new recipe |
| `GET` | `/api/recipes-list/<id>/` | Retrieve a specific recipe |
| `PUT` | `/api/recipes-list/<id>/` | Replace an entire recipe |
| `PATCH` | `/api/recipes-list/<id>/` | Partially update a recipe |
| `DELETE` | `/api/recipes-list/<id>/` | Delete a recipe |

### Recipe Fields

- `id` - Unique identifier
- `title` - Recipe name
- `description` - Recipe details
- `created_at` - Creation timestamp
- `author` - Author ID

### Example: Create a Recipe

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/recipes-list/ `
  -H "Authorization: Token YOUR_TOKEN" `
  -H "Content-Type: application/json" `
  -d '{"title":"Pizza","description":"Delicious Tuna Pizza","author":1}'
```

## Testing

### Run Tests

Execute all tests with Django:

```powershell
python manage.py test
```

### Generate Test Coverage Report

Run tests with coverage tracking:

```powershell
coverage run manage.py test
```

Display the detailed coverage report:

```powershell
coverage report -m
```

## Project Structure

```text
core/                     Django project settings and configuration
recipes_app/              Main recipe application module
recipes_app/api/          API serializers, views, and URL routing
recipes_app/tests/        Unit and integration tests
db.sqlite3                SQLite database file
manage.py                 Django management script
requirements.txt          Python package dependencies
README.md                 This file
```