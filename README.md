# Django Practice Project

This repository is dedicated to practicing Django development. It contains a basic Django setup with a sample application to explore various features of the framework.

## Purpose

The main goal of this project is to provide a clean environment for learning and experimenting with:
- Django Project and App structure.
- Models, Views, and Templates.
- Django Admin interface.
- Database migrations with SQLite.
- Dependency management with Pipenv.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python** (version 3.10 or higher recommended)
- **Pipenv** (can be installed via pip: `pip install pipenv`)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django
```

### 2. Install Dependencies

This project uses `pipenv` to manage dependencies and virtual environments.

```bash
pipenv install
```

### 3. Activate the Virtual Environment

```bash
pipenv shell
```

---

## Running the Project

Navigate to the `project` directory where `manage.py` is located:

```bash
cd project
```

### Database Migrations

Before running the server for the first time, apply the initial migrations:

```bash
python manage.py migrate
```

### Create a Superuser (Optional)

To access the Django Admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### Start the Development Server

#### Windows (PowerShell)
```powershell
python manage.py runserver
```

#### Linux / macOS (Bash)
```bash
python manage.py runserver
```

Once the server is running, you can access the project at `http://127.0.0.1:8000/`.

---

## Project Structure

- `project/`: The main Django project directory.
  - `manage.py`: Django's command-line utility.
  - `project/`: Project configuration (settings, URLs, WSGI/ASGI).
  - `firstapp/`: A sample Django application.
- `Pipfile` & `Pipfile.lock`: Dependency management files.
