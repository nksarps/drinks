# Drinks

A Django REST Framework API for managing drinks.

## Requirements

- Python 3.10+
- pip

## Setup

```bash
# clone the repo
git clone https://github.com/nksarps/drinks.git
cd drinks

# create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# run the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

Base path: `/api/v1/drinks/`

| Method | Endpoint                | Description          |
|--------|--------------------------|-----------------------|
| GET    | `/api/v1/drinks/`         | List all drinks       |
| POST   | `/api/v1/drinks/`         | Create a new drink    |
| GET    | `/api/v1/drinks/<id>`     | Retrieve a drink      |
| PUT    | `/api/v1/drinks/<id>`     | Update a drink        |
| DELETE | `/api/v1/drinks/<id>`     | Delete a drink        |

### Drink object

```json
{
  "id": 1,
  "name": "Mojito",
  "description": "A refreshing mix of rum, mint, and lime"
}
```

## Admin

Create a superuser to access the Django admin at `/admin/`:

```bash
python manage.py createsuperuser
```

## Project Structure

- `main/` — Django project configuration (settings, root URLs)
- `drinks/` — Drinks app (model, serializer, views, URLs, admin)
