from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('sponsor', 'Sponsor'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


    def __str__(self):
        return self.username 
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1.Users'