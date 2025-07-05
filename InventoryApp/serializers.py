from rest_framework.serializers import ModelSerializer
from .models import Inventory
from django.contrib.auth.models import User

class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user