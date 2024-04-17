from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('add_to_route/', views.add_to_route, name='add_to_route'),
    path('add_personal_data/', views.add_personal_data, name='add_personal_data'),
    path('hotel_filter/', views.hotel_filter, name='hotel_filter'),
    path('transport_booking/', views.transport_booking, name='transport_booking'),
]