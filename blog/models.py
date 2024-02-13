from asyncio import AbstractServer
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, db_index=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    about  = models.TextField()
    

    def __str__(self):
        return self.username
    pass
     

class Category(models.Model):
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title    


class Tag(models.Model):
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    
    def __str__(self):
        return self.title
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title',unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
   # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
