from django.db import models
from django.contrib.auth.models import User
class description(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    def __str__(self):
        return self.content[:]
    
class frontImage(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.photo.url)
    
class CV(models.Model):
    document = models.FileField(upload_to='cv/')
    
    def filename(self):
        return self.document.name.split('/')[-1]
    
    def __str__(self):
        return str(self.document.url)

class Timeline_Details(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.TextField()
    subject = models.TextField()
    timeline = models.TextField()
    desc = models.TextField()
    
    def __str__(self):
        return self.company_name
    
from django.db import models

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    desc = models.TextField()
    link = models.TextField()
    image = models.ImageField(upload_to='projects/')
    video = models.FileField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.TextField()
    body = models.TextField()
    
    def __str__(self):
        return self.body[:]
    
class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    def mark_as_seen(self):
        self.seen = True
        self.save()
    
    def __str__(self):
        return self.name[:]
