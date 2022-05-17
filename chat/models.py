import uuid
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.UUIDField(default=uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
