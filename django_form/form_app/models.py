from django import forms
from django.db import models


class Entrepreneur(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255, blank=True)
    ico = models.CharField(max_length=8)
