#user/models.py
from django.db import models
from django.contrib.auth.models import AbastractUser

# Create your models here.
class UserModel(AbastractUser):
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')

