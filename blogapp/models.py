from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=0)
    image = models.ImageField(upload_to ='img')

    def __str__(self):
        return self.title
    

class Detail(models.Model):
    title = models.CharField(max_length=255)
    nom_auteur = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=0)
    image = models.ImageField(upload_to = 'img')
    article = models.TextField()
    categories_id = models.ForeignKey('Categorie',on_delete=models.CASCADE, related_name="categorie_detail")


    def __str__(self):
        return self.title