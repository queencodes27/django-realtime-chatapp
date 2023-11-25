from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name
class Room(models.Model):
    name = models.CharField(max_length=200)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
