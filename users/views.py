from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework import generics
from users.models import User

class UserCreateView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserSerializer