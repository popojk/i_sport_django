"""
Test for models
"""
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(username='popojk', password='12345678'):
    """Create and return a user"""
    return get_user_model().objects.create_user(username, password)

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_username_successful(self):
        """Test creating a user with an username is successful."""
        username = 'test'
        password = '12345678'
        user = get_user_model().objects.create_user(
            username = username,
            password = password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_username_raises_error(self):
        """Test that creating a user without an username raises a Value Error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )