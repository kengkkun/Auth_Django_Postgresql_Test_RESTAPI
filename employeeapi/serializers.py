# api <-> mobile app/ web/ app./ json/xml
from rest_framework import serializers
from .models import Employee, IotDevices

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = IotDevices
        fields = '__all__'