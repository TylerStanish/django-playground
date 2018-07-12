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


class SecretView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        return Response('Protected resource')

