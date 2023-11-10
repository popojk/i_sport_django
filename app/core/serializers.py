from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers, exceptions
from django.utils.translation import gettext_lazy as _

from core.models import User

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)
    
    def _validate_username(self, username, password):
        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)
        
        return user
    
    def get_auth_user_using_orm(self, username, password):
        return self._validate_username(username, password)
    
    def get_auth_user(self, username, password):
        return self.get_auth_user_using_orm(username, password)
    
    @staticmethod
    def validate_auth_user_status(user):
        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)
        
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = self.get_auth_user(username, password)

        if not user:
            msg = _('Unable to login with provided credentials.')
            raise exceptions.ValidationError(msg)
        
        # Did we get back an active user?
        self.validate_auth_user_status(user)

        attrs['user'] = user
        return attrs
    
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        """create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname')
        read_only_fields = ('id', 'username')