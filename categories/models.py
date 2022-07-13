from django.db import models
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False
       )
    nome = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


