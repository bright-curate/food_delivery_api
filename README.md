
FOOD DELIVERY / RESTAURANT API

PROJECT IDEA:
The goal of this project is to build a RESTful API for a food delivery platform.
Users will be able to browse restaurants, view menus, place orders, and track their orders.
Admin users can manage restaurants, menu items, and update order statuses. The API could serve as the backend for a web or mobile food delivery application.
FEATURES:
For Users:
Register and login
Browse restaurants
View menus
Place orders
View order history
For Admins:
Add, Update, and delete restaurants
Add, update and delete menu items
Update order status (Pending, Preparing, Delivered)
Security
Token-based authentication (DRF TokenAuthentication)
Role-based access control (users vs admins)

MODELS
Users: Extends Django's default user with role (user/admin)
Restaurant: name, address, cuisine type
MenuItem: Restaurant (FK), name, description
Order: User (FK), restaurant (FK), items (many-to-many with quantity), total price, status
