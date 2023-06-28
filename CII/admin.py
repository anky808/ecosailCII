from django.contrib import admin

from CII import models
from CII.models import VesselOwnerMaster, ContactTypeMaster

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.VesselOwnerMaster)
admin.site.register(models.ContactTypeMaster)