from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import FieldDoesNotExist
# Create your models here.
class CustomUser(AbstractUser):
    pass