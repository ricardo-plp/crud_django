from django.db import models

# Create your models here.

class Questions(models.Model):
    text = models.TextField()
    class Meta:
        db_table = "questions"
