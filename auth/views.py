from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class SecretView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        return Response('Protected resource')

