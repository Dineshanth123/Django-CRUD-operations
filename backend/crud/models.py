from django.db import models

# Create your models here.
class Courses(models.Model):
  name=models.CharField(max_length=200)
  tutor=models.CharField(max_length=200)

  def __str__(self):
    return self.name