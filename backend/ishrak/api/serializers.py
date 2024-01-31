from rest_framework import serializers
from .models import ItemsModel
from django.contrib.auth.models import User
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']