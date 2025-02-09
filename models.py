from django.db import models

# Create your models here.
class Donor(models.Model):
  name =models.CharField(max_length=100)
  age= models.IntegerField()
  blood_group=models.CharField(max_length=5)
  contact =models.CharField(max_length=15)
  city =models.CharField(max_length=50)

  def __str__(self):
      return self.name 