A secure REST API implementation with JWT authentication and Role-Based Access Control (RBAC) using Django and PostgreSQL.

## Features

- ✅ User registration and login with JWT tokens
- 🔒 Role-Based Access Control (Admin and User roles)
- 🛡️ Password hashing with bcrypt
- 📦 CRUD operations for projects with role restrictions
- 🐘 PostgreSQL database backend

## Table of Contents

1. [Installation](#Installation:)
2. [Dependencies](#Install-dependencies:)
3. [API Endpoints](#api-endpoints)

## Installation:

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip

### Setup Steps

1. Clone the repository:

```bash
git clone https://github.com/KPDileepKumar/jwt_rbac.git
cd jwt_rbac
```

2. Create and activate virtual environment:

```bash
python -m venv venv
# On Windows:
envname\Scripts\activate
# On macOS/Linux:
source envname/bin/activate
```

## Install-dependencies:

```bash
python -m pip install -r requirements.txt
```

## Set up PostgreSQL database

```bash
createdb jwt_rbac
```

(or)
Manually create jwt_rbac Database in your Databases inside your Server

## Run migrations:

```bash
python manage.py migrate
```

## Run the development server:

```bash
python manage.py runserver
```

## api-endpoints

Endpoint -- Method -- Description -- Access  
/api/register/ -- POST -- Register new user -- Public  
/api/login/ -- POST -- Login and get JWT token -- Public  
/api/projects/ -- GET -- List all projects -- Authenticated  
/api/projects/ -- POST -- Create new project -- Admin only  
/api/projects/&lt;id&gt;/ -- GET -- Get project details -- Authenticated  
/api/projects/&lt;id&gt;/ -- PUT -- Update project -- Admin only  
/api/projects/&lt;id&gt;/ -- DELETE -- Delete project -- Admin only
