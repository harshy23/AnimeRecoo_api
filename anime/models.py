from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Useranime(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE )
    favgenres = models.TextField(default="[]", blank=True, null=True)