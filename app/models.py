from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        Automatically generates a Token whenever a User is created
    """
    if created:
        Token.objects.create(user=instance)


class Address(models.Model):
    """
        A sample model of an Address
    """
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s %s' % (self.street, self.city, self.state, self.country)

    class Meta:
        verbose_name_plural = "Addresses"
