from django.contrib.auth.models import User
from django.db import models

class AdditionalUserInformation(models.Model):
    userType = models.IntegerField()
    userId = models.CharField(max_length=6)
    username = models.CharField(max_length=30)