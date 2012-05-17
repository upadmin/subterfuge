from django.db import models
from django import forms

class installed(models.Model):
    name        = models.CharField(max_length=300)
    active      = models.CharField(max_length=300)
    
    
class iptrack(models.Model):
    address     = models.CharField(max_length=300)
    injected    = models.CharField(max_length=300)
    
    
    


