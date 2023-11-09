from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # Add your additional fields here
    nickname = models.CharField(
        max_length=64, null=True, blank=True, verbose_name='nickname'
    )
    email = models.EmailField(max_length=255, blank=True)
    is_owner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)