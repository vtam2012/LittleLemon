from django.contrib.auth.models import User
from rest_framework import serializers
from .models import booking, menu

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
