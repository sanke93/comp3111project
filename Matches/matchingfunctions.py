'''
Created on Apr 8, 2014

@author: Mr. Awesomepants
'''
from User_Profile.models import UserProfile, Skills, Desires
from django.contrib.auth.models import User
from Matches.models import Matches
def match_user(person):
    '''This function takes as inpudt user class'''
    #first figure out what user wants
    for x in Desires.objects.filter(user= person):
        r=Matches(user1=person)
        #Iterate Through the list of skills other people have
        for y in Skills.objects.filter(skill= x.wants):
            #Now we check and see what the other person wants
            for z in Desires.objects.filter(user=y.user):
                for ab in Skills.objects.filter(user=person):
                    if(z.wants==ab.skill && y.user!=person):
                        r.user2 = y.user
                        
                        r.offering = ab.skill
                        r.recieving =y.skill
                        r.save()
        
    
    
    





