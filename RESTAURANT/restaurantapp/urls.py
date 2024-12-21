from django.urls import path
from . import views
from restaurantapp import views

urlpatterns = [
    path('', views.menu_page, name='home'),
    path('place_order/', views.place_order, name='place_order'),
]
