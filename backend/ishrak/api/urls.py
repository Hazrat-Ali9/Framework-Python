from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'items', views.DataList, basename='item')

urlpatterns = [
    path('items/',views.DataList.as_view()),
    path('items/<int:pk>/', views.DataUpdateDelete.as_view()),
    path('items/search/', views.ProductSearchAPIView.as_view(), name='product-search'),
    path('admin/', views.AdminDashboard.as_view(), name='admin_dashboard'),
]