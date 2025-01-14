from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="ki~tech-home" ),
    path('about/', views.about, name="ki~tech-about" ),
    path('contact/', views.contact, name="ki~tech-contact" ),
    path('service/', views.service, name="ki~tech-service" ),
    path('course/', views.course, name="ki~tech-course" ),
    path('login/', views.login, name="ki~tech-login" ),
]