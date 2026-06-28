# Blog Application — Django

A full-featured blog platform with role-based access control and group-based permissions built with Django.

## Roles & Permissions
- **Admin** — Full access, manage all articles, comments and users
- **Author** — Create, edit and delete own articles
- **Reader** — Read articles and post comments

## Models
- **CustomUser** — Extended Django user with role field
- **Article** — Blog post with author, category and content
- **Comment** — User comments linked to articles

## Features
- Custom authentication system
- Group-based permissions (Django Groups)
- Custom login required decorator
- Ownership check — authors can only edit/delete own articles
- Admin can delete any article or comment
- Category based article organization

## Tech Stack
- Python
- Django
- SQLite
- Bootstrap 5
- HTML/CSS

## How to Run
cd Blog_Application
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Project Structure
```
Blog_Application/
├── Accounts/      # Auth, registration, login
├── blog/          # Articles, comments, permissions
├── templates/     # Base template
└── manage.py
```
