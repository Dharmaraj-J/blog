from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime


# Create your models here.



class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)