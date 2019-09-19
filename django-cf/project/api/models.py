from django.db import models
from django.utils import timezone

class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
