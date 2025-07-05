from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Inventory
from .serializers import InventorySerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class InventoryViewset(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class CategoryListView(ListAPIView):
    def get_queryset(self):
        category = self.kwargs['cg']
        return Inventory.objects.filter(category__iexact = category)
    
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

class PriceSortView(ListAPIView):
    queryset = Inventory.objects.all().order_by("-price")
    serializer_class = InventorySerializer  
    permission_classes = [IsAuthenticated]
    
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer