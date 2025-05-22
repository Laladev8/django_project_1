from django.db import models

# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    date=models.DateTimeField()