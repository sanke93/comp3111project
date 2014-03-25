from django.db import models
from django.db.models.signals import post_save
from django.db.auth.models import User
#signals sends out information to other parts of the program
#auth is authentication. I'm not quite sure how it works yet
# Create your models here.
class UserProfile(models.Model):
#This is a start of the user profile page
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'NA')
    )
   
#basic user fields, more probably for later
    user = models.ForeignKey(User, unique=True)
    birth_date = models.DateField(null= True)
    address = models.CharField(max_length=150, null=True)
    skills = models.ForeignKey(Skills, null=True)
    desires = models.ForeignKey(Desires, null=True)
    about = models.CharField(max length=400, null=True )
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
        
post_save.connect(create_user_profile, sender=User)