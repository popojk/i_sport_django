from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dj_rest_auth import views as dj_views
from dj_rest_auth.serializers import TokenSerializer
from drf_yasg.utils import swagger_auto_schema

from core.serializers import UserLoginSerializer, UserDetailsSerializer

class LoginView(dj_views.LoginView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_description='Get access token with username and password.\n'
                         'If token not exists, create a new one, otherwise return the existing one.',
                         request_body=UserLoginSerializer,
                         response={200: TokenSerializer},
                         security=[]
                         )
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)
    
class LogoutView(APIView):
    """
    Calls Django logout method and delete the Token object
    """
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'dj_rest_auth'

    @swagger_auto_schema(operation_description="Delete user's access token",
                         response={200: 'Successfully logged out'},)
    def post(self, request, *args, **kwargs):
        return self.logout(request)
    
    def logout(self, request):
        try:
            print(request.user.auth_token)
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        response = Response(
            {'detail': _('Successfully logged out.')},
            status=status.HTTP_200_OK,
        )
        return response
    
class UserDetailsView(dj_views.UserDetailsView):
    @swagger_auto_schema(operation_description="Get user detail data.",
                         response={200: UserDetailsSerializer(many=False)})
    def put(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)
    
    @swagger_auto_schema(operation_description="Update user data.",
                         response={200: UserDetailsSerializer(many=False)})
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_400_NOT_FOUND)
    
class PasswordChangeView(dj_views.PasswordChangeView):
    @swagger_auto_schema(operation_description="Change user's password.",
                         response={200: 'Password changed successfully.'})
    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)
    

    



