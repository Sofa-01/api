from django.shortcuts import render, redirect
from .models import PersonalData
from .forms import PersonalDataForm
from .models import Hotel
from .forms import TransportBookingForm
from .models import TransportRoute


def transport_booking(request):
    if request.method == 'POST':
        form = TransportBookingForm(request.POST)
        if form.is_valid():
            route = form.cleaned_data['route']
            departure_date = form.cleaned_data['departure_date']
            return_date = form.cleaned_data['return_date']
            passengers_count = form.cleaned_data['passengers_count']

            # Сохранение данных бронирования в базе данных
            booking = TransportRoute.objects.create(route=route, departure_date=departure_date,
                                                      return_date=return_date, passengers_count=passengers_count)

            # Дополнительная логика, например, перенаправление на страницу подтверждения
            return redirect('booking_confirmation')
    else:
        form = TransportBookingForm()
    return render(request, 'transport_booking.html', {'form': form})


def add_personal_data(request):
    if request.method == 'POST':
        form = PersonalDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonalDataForm()
    return render(request, 'add_personal_data.html', {'form': form})
# Create your views here.

def hotel_filter(request):
    hotels = Hotel.objects.all()

    # Получение параметров фильтрации из GET-запроса
    stars = request.GET.get('stars')
    guests = request.GET.get('guests')
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')

    # Применение фильтров к запросу отелей
    if stars:
        hotels = hotels.filter(stars_count=stars)
    if guests:
        hotels = hotels.filter(places_count__gte=guests)
    if check_in:
        hotels = hotels.filter(available_rooms__check_in__lte=check_in)
    if check_out:
        hotels = hotels.filter(available_rooms__check_out__gte=check_out)

    return render(request, 'hotel_filter.html', {'hotels': hotels})