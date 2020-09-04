from django.db import models
from django.contrib.auth.models import AbstractUser

class Twitter_user(AbstractUser):
    follow = models.ManyToManyField("self", symmetrical=False)

def __str__(self):
    return self.title


