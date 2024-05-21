from django.db import models
from ckeditor.fields import RichTextField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    imageSrc = models.ImageField(upload_to="hero")
    resume = models.FileField(upload_to="resume")
    description = RichTextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    imageSrc = models.ImageField(upload_to="project_images")
    description = RichTextField()
    link = models.URLField(blank=True)
    source = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    imageSrc = models.ImageField(upload_to="project_images")

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    startDate = models.CharField(max_length=50)
    endDate = models.CharField(default="Present", max_length=50)
    location = models.CharField(max_length=200)
    imageSrc = models.ImageField(upload_to="company_logos")
    experiences = RichTextField()
    def __str__(self):
        return self.organisation



class SocialMedia(models.Model):
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    linkedin_link = models.URLField()
    github_link = models.URLField()
    twitter_link = models.URLField()
    mail = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return self.mail
    

class TitleString(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    issue_date = models.DateField()
    description = models.TextField()
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email