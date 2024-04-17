from django.views.generic import TemplateView
from .models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        # Здесь вы можете выполнить дополнительные действия после создания пользователя
    return render(request, 'create.html')

class MainPage(TemplateView):
    template_name = 'main.html'


class Signin(TemplateView):
    template_name = "signin.html"


class Signup(TemplateView):
    template_name = "signup.html"


class Create(TemplateView):
    template_name = 'create.html'


class Favorite(TemplateView):
    template_name = 'favorite.html'

class HotelReserv(TemplateView):
    template_name = 'hotelreserv.html'

class TransReserv(TemplateView):
    template_name = 'transreserv.html'

class Personal(TemplateView):
    template_name = 'personal.html'
