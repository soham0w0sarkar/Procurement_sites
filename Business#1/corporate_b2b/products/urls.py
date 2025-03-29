from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='list'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('category/<slug:category>/', views.category_view, name='category'),
]