from rest_framework import serializers
from rest_framework import employees

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        field = '__all__'
