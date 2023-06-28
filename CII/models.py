from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """ Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    def __str__(self):
        """ Return string representations of our user"""
        return self.email

class VesselOwnerMaster(models.Model):
    Company_Name = models.CharField(max_length=255)
    Company_IMO_Number = models.IntegerField()
    Country_Registration = models.CharField(max_length=150)
    Company_Address = models.TextField()
    Company_identification_Number = models.IntegerField()
    Company_Description = models.TextField()
    Add_contact_details = models.CharField(max_length=20)


class ContactTypeMaster(models.Model):
    contact_type_name = models.CharField(max_length=255)
    contact_description = models.TextField(max_length=255)
    short_name = models.CharField(max_length=25)
