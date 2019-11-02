from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class MyUser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name =models.CharField(max_length=128)
    email =models.EmailField(unique=True)
    password = models.CharField(max_length=32)



class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_website = models.URLField(blank =True)
    profile_pic  = models.ImageField(upload_to ='profile_pics',blank="True")
    def __str__(self):
        return self.user.username
