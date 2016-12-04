from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=14)
    def __str__(self):
        return self.name + self.number
