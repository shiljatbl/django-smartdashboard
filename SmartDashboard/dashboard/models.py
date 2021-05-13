from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    power_status = models.BooleanField(default=False)
    light_type = models.CharField(max_length=255, default='Light')
   
    def __str__(self):
        return self.name


class DeviceLEDStrip(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    power_status = models.BooleanField(default=False)
    light_type = models.CharField(max_length=255, default='Light')
   
    def __str__(self):
        return self.name