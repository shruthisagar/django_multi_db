from datetime import datetime
from django.db import models


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()