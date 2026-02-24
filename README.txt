# 📘 Multi-Role Blog Platform

A role-based content management system (CMS) built with **Django** and **PostgreSQL**, featuring an approval-driven author promotion workflow, structured relational data modeling, and cloud deployment on Railway.

---

## 🚀 Overview

This project is a production-ready blog platform designed to simulate real-world backend architecture. It supports multiple user roles with controlled publishing permissions and a structured approval system.

The application demonstrates:

* Role-Based Access Control (RBAC)
* Relational database design
* Approval workflow systems
* Production deployment practices
* Environment-based configuration

---

## 🧠 Key Features

### 👤 User Roles

* **User (Reader)** – Can read blogs and request author access.
* **Author** – Can create and manage blog posts.
* **Manager** – Can approve or reject author role requests.

### 🔄 Author Promotion Workflow

* Users submit a request to become an Author.
* Managers review pending requests.
* Approved users are automatically promoted.
* Old roles are removed to maintain clean access hierarchy.

### 📝 Blog System

* Create, edit, delete blog posts (Author role).
* Published/unpublished status control.
* Slug-based detail pages.

### 💬 Comment System

* Authenticated users can comment.
* Comments linked via foreign key relationships.
* Ordered by creation time.
* Flash messaging on submission.

### 🔐 Access Control

* Django Groups for RBAC
* Custom role-based decorators
* Protected routes
* Secure role transition logic

---

## 🏗 Architecture & Design Decisions

### Framework

* **Django (MVT pattern)**

  * Models → Data logic
  * Views → Business logic
  * Templates → Presentation layer

### Database

* **PostgreSQL**

  * ACID-compliant
  * Strong relational integrity
  * Foreign key constraints
  * Production-grade performance

### Design Patterns Used

* Role-Based Access Control (RBAC)
* Workflow/State Machine (Pending → Approved → Rejected)
* Separation of Concerns
* Environment-based configuration
* Stateless request handling

---

## 🛠 Tech Stack

* Python
* Django
* PostgreSQL
* Gunicorn
* Whitenoise
* Railway (Deployment)
* Git / GitHub

---

## ⚙️ Installation (Local Development)

### 1. Clone the repository

```bash
git clone https://github.com/Marsh4444/-blog-platform.git

cd yourrepo
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 🌍 Production Deployment

Deployed using:

* Railway
* PostgreSQL
* Gunicorn
* Whitenoise for static files

Production configuration includes:

* `DEBUG = False`
* Environment variables for secrets
* Secure database URL handling
* Static file collection via `collectstatic`

---

## 📊 Database Structure

Key Relationships:

* User → Blog (One-to-Many)
* Blog → Comment (One-to-Many)
* User → RoleRequest (One-to-Many)

RoleRequest acts as a workflow model:

* Pending
* Approved
* Rejected

This ensures controlled permission escalation.

---

## 📈 Scalability Considerations

If scaling further, improvements would include:

* Redis caching
* Pagination for large datasets
* Celery for background tasks
* S3 for media storage
* Read replicas for database
* API layer with Django REST Framework
* CI/CD integration
* Automated testing suite

---

## 🎯 What This Project Demonstrates

* Backend system design
* Relational database modeling
* Access control architecture
* Production deployment workflow
* Structured code organization
* Clean separation of concerns

---

## 📌 Future Improvements

* Comment moderation panel
* Nested comment replies
* Email notifications
* Activity logging
* Unit & integration tests
* REST API version
* Frontend separation (React)

---

## 📜 License

This project is built for educational and professional portfolio purposes.

