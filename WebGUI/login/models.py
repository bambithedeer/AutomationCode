
from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")
    type = models.IntegerField(default=5)
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    age = models.IntegerField(default=0)
    addr = models.CharField(max_length=200, default="")
