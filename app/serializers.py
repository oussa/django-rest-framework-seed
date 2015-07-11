from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url', 'street', 'city', 'state', 'country')