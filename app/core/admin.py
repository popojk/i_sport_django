from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    """define the admin page for users"""
    ordering = ['id']
    list_display = ['email', 'username']

admin.site.register(models.User, UserAdmin)
