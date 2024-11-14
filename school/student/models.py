from django.db import models

# Create your models here.
class stud(models.Model):
    s_name = models.CharField(max_length=30)
    s_aadhar = models.CharField(max_length=30)
    s_class = models.CharField(max_length=30)
    s_division = models.CharField(max_length=30)
    s_egrantid = models.CharField(max_length=30)
    s_category = models.CharField(max_length=30)
    s_gender = models.CharField(max_length=30)