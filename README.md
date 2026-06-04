# Django Practice Project

This repository is dedicated to practicing Django development. It contains a basic Django setup with a sample application to explore various features of the framework.

## Purpose

The main goal of this project is to provide a clean environment for learning and experimenting with:
- Django Project and App structure.
- Models, Views, and Templates.
- Django Admin interface.
- **PostgreSQL Integration via Docker.**
- **Environment Variable Management with `django-environ`.**
- Dependency management with Pipenv.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python** (version 3.10 or higher recommended)
- **Pipenv** (`pip install pipenv`)
- **Docker & Docker Compose**

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django
```

### 2. Install Dependencies

```bash
pipenv install
```

### 3. Setup Environment Variables

Copy the example environment file and update it if necessary:

```bash
cp .env.example .env
```

### 4. Start the Database

This project uses PostgreSQL running in a Docker container.

```bash
docker-compose up -d
```
*Note: The database is configured to run on host port **5433** to avoid conflicts.*

---

## Running the Project

### Database Migrations

Apply migrations to the PostgreSQL database:

```bash
python -m pipenv run python project/manage.py migrate
```

### Create a Superuser (Optional)

```bash
python -m pipenv run python project/manage.py createsuperuser
```

### Start the Development Server

```bash
python -m pipenv run python project/manage.py runserver
```

Once the server is running, you can access the project at `http://127.0.0.1:8000/`.

---

## Project Structure

- `project/`: The main Django project directory.
  - `manage.py`: Django's command-line utility.
  - `project/`: Project configuration (settings, URLs, WSGI/ASGI).
  - `firstapp/`: A sample Django application.
- `docker-compose.yml`: Docker configuration for the PostgreSQL database.
- `.env.example`: Template for environment variables.
- `Pipfile` & `Pipfile.lock`: Dependency management files.
