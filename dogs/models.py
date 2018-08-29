from django.db import models

# Create your models here.

class guessed_result(models.Model):
   guess_date = models.DateTimeField()
   breed = models.CharField(max_length=50)
   accurancy = models.CharField(max_length=4)
   correct = models.BooleanField(default=False)   