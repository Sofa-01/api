"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('signin/', views.Signin.as_view(), name='signin'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('create/', views.Create.as_view(), name='create'),
    path('favorite/', views.Favorite.as_view(), name='favorite'),
    path('hotelreserv/', views.HotelReserv.as_view(), name='hotelreserv'),
    path('transreserv/', views.TransReserv.as_view(), name='transreserv'),
    path('personal/', views.Personal.as_view(), name='personal'),
    path('admin/', admin.site.urls),
]

