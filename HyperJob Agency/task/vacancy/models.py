from django.db import models
from django.conf import settings


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)