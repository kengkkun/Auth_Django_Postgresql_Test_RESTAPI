from django.db import models

# Create your models here.


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    cleaned = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)

class IotDevices(models.Model):
    device_name = models.CharField(max_length=20)
    mac_adrress = models.BigIntegerField()
    factory_id = models.CharField(max_length=50)
    approval_status = models.CharField(max_length=3)
    installed_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    gateway_id = models.IntegerField()
    public_space_id = models.IntegerField()
    room_id = models.IntegerField()
    supported_device_id = models.IntegerField()
