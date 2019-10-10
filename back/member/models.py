from django.db import models
    

class Menber (models.Model):
    Fristename = models.CharField(max_length=20)
    LASTNAME = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Fristename