from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from app.models import Address
from app.serializers import UserSerializer, AddressSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Only admin can view users. Others get a 401 unauthorized
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
        List, Get, Create, Update or Delete an Address
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer