from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    balance=models.IntegerField(min('1000'))
    accno=models.IntegerField()
    username=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
         return self.username




