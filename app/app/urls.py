"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import LoginView, LogoutView, UserDetailsView, RegisterView,PasswordChangeView

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title='Isport API',
        default_version='v1',
        description='API documentation',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@localhost'),
        license=openapi.License(name='BSD License')
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    # dj_rest_auth
    path('api/v1/login/', LoginView.as_view(), name='rest_login'),
    path('api/v1/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/v1/register', RegisterView.as_view(), name='rest_register'),
    path('api/v1/user', UserDetailsView.as_view(), name='rest_user_details'),
    path('api/v1/password/change/', PasswordChangeView.as_view(), 
         name='rest_password_change'),
    # swagger
    path('api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
