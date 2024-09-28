from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  
    path('phones/', views.phone_list, name='phone_list'),  
]
