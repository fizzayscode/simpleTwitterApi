from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name= models.CharField(max_length=100,null=True)
    email= models.EmailField(unique=True,null=True)
    bio= models.TextField(null=True,blank=True)

    # avatar=models.ImageField(default='profile.png')

    # just because the foreignkey calls the object from here itself so i had to turn it to a string 
    def __str__(self):
        return str(self.name)

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_DEFAULT, default=None, null=True ,related_name='tweets')
    created=models.DateField(auto_now_add=True)
    desc=models.CharField(max_length=280)
    likes=models.IntegerField(default=0, null=True, blank=True)
    

    def __str__(self):
      return self.desc

# Create your models here.
