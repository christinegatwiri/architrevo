from django.db import models
from datetime import datetime 

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200,default="null")
    image1 = models.ImageField(upload_to = 'images/portfolio', default=None)
    image2 = models.ImageField(upload_to = 'images/portfolio', default=None)
    image3 = models.ImageField(upload_to = 'images/portfolio', default=None)
    image4 = models.ImageField(upload_to = 'images/portfolio', default=None)
    location = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class HousePlans(models.Model):
    title = models.CharField(max_length=200,default="null")
    images = models.ImageField(upload_to = 'images/houseplans', default=None)
    location = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Services(models.Model):
    service_pic = models.ImageField(upload_to = 'images/portfolio', default=None)
    service_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class NewsletterList(models.Model):
    email_address = models.CharField(max_length=200)

class Applications(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=400)

class Blog(models.Model):
    thumbnail = models.ImageField(upload_to = 'images/blog', default=None)
    date = models.DateTimeField(default=datetime.now, blank=True)
    post = models.CharField(max_length=10000)


