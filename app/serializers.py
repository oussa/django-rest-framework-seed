from django.contrib.auth.models import User
from rest_framework import serializers


# Sample Serializer: UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')