from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class HomePageImage(models.Model):
    image = models.ImageField(upload_to='home_page_images/')

    def __str__(self):
        return self.image
    


class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about_us_images')

    def __str__(self):
        return f'Gallery image {self.id}'

class FoodMenu(models.Model):
    FOOD_TYPE_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON_VEG', 'Non-Vegetarian'),
    ]
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='food_menu_images/')
    food_type = models.CharField(max_length=7, choices=FOOD_TYPE_CHOICES,default='Veg')

    def __str__(self):
        return self.name
    
class Chef(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to='chef_images/')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    proffession = models.CharField(max_length=255,default="Chef")
    photo = models.ImageField(upload_to='Testimonials',default="image")
    Description = models.TextField()

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/',null=True)

    def __str__(self):
        return self.title
    

class MyUserManager(BaseUserManager):
    def create_user(self, mobile_number, full_name, password=None):
        if not mobile_number:
            raise ValueError('The Mobile Number is required')
        if not full_name:
            raise ValueError('The Full Name is required')
        
        user = self.model(mobile_number=mobile_number, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, full_name, password=None):
        user = self.create_user(mobile_number, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.mobile_number

    @property
    def is_staff(self):
        return self.is_admin