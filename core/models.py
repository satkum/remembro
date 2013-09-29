from django.db import models
from django.contrib.auth.models import User

class Meow(models.Model):
    text = models.CharField(max_length=160)
    alarm_time = models.DateTimeField(null=True)
    user = models.ForeignKey(User)
    ts = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    
    
