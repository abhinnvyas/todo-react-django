from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=100, null=False)
    isDone = models.BooleanField(default=False)
