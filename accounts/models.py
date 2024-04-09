from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Choices
    IDENTIFICATION_CHOICES = (
        ('CC', 'Cédula de Ciudadanía'),
        ('PEPFF', 'Pasaporte'),
    )
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    USER_TYPE_CHOICES = (
        ('Gerente', 'Gerente'),
        ('Director', 'Director'),
        ('Capataz', 'Capataz'),
        ('Peones', 'Peones'),
        ('Ayudantes', 'Ayudantes'),
    )

    # Custom fields
    #photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    identificationType = models.CharField(max_length=5, choices=IDENTIFICATION_CHOICES, blank=True, null=True)
    identificationNumber = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    userType = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES ,  blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)