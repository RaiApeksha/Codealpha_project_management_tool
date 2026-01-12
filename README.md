Project Management Tool (Django)

A full-stack collaborative project management tool, built with Django, supporting authentication, project boards, task assignment, comments, notifications, and real-time updates.
This project is designed as a learning-to-production journey, covering backend, frontend, and real-time features.

Features :
Core Features 
- User authentication (Register / Login / Logout)
- Create and manage projects
- Add members to projects
- Task management with statuses:
* To Do
* In Progress
* Done
- Assign tasks to project members
- Comment system inside tasks

Project dashboard:
Advanced Features
- Notifications system
- Real-time updates using Django Channels & WebSockets
- AJAX-based interactions (no page reloads)
- Clean UI layout

Tech Stack:
- Backend
- Python 
- Django 
- Django Channels
- SQLite (development)

Frontend:
- HTML5
- CSS (custom Trello-style UI)
- JavaScript (AJAX)

Installation & Setup:
Create Virtual Environment: python -m venv venv
Activate it: Windows(venv\Scripts\activate)
             Mac/Linux(source venv/bin/activate)

Install Requirements:
- pip install django
- pip install django channels

Apply Migrations:
- python manage.py makemigrations
- python manage.py migrate

Run Development Server:
- python manage.py runserver
