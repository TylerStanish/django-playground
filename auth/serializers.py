from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # we include write_only=True here to prevent the hashed password from being included in the JSON
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
