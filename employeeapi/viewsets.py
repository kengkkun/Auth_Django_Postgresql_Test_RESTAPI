from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class ControllerViewset(viewsets.ModelViewSet):
    queryset = models.IotDevices.objects.all()
    serializer_class = serializers.DeviceSeriallizer

# list(), retrive(), create(), update(), destroy()