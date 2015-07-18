from django.db import models
from django.db.models import Model

class User(models.Model):
    phoneNumber = models.PositiveSmallIntegerField(max_length=10,default=None)
    zipCode = models.PositiveSmallIntegerField(max_length=5,default=None)
    sendTime = models.PositiveSmallIntegerField(max_length=4,default=None)
    cronjobID = models.PositiveSmallIntegerField(max_length=4,default=None)
    
    def __unicode__(self):
		return str(self.phoneNumber)