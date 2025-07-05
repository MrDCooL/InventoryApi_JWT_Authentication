"""
URL configuration for InventoryApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from InventoryApp.views import InventoryViewset,CategoryListView,PriceSortView,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register("inventory",InventoryViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('inventory/category/<str:cg>/',CategoryListView.as_view()),
    path('inventory/price/sort/',PriceSortView.as_view()),
    path('inventory/api/token',TokenObtainPairView.as_view()),
    path('inventory/api/refresh',TokenRefreshView.as_view()),
    path('inventory/api/register',RegisterView.as_view())
]
