WEEK 1 — Project Setup
Goal of Week 1
Set up the Django project, apps, and the basic tools you need (like Django REST Framework and token authentication).

Explanation (Simple)
I thought of 1 week as building the foundation of my house.

Before i add walls, furniture, decorations — i need a strong structure.
So this week you will:

Install Django + DRF
Create project folders
Create three apps
Set up authentication
Set up your database models (blueprints)

STEP 1 — Create Django Project

django-admin startproject food_delivery_apicd food_delivery_api

STEP 2 — Create Apps

python manage.py startapp users
python manage.py startapp restaurants
python manage.py startapp orders

STEP 3 — Install Django REST Framework + Token Auth
Add to settings.py:


STEP 4 — Add DRF + Token Config

STEP 5 — Create User Model

STEP 6 — Tell Django to Use This New User Model

