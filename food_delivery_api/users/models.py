from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def is_admin(self):
        return self.role == 'admin' or self.is_staff or self.is_superuser
