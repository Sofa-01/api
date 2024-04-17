from django import forms
from .models import PersonalData
from .models import TransportRoute

class TransportBookingForm(forms.Form):
    route = forms.ModelChoiceField(queryset=TransportRoute.objects.all(), label='Маршрут')
    departure_date = forms.DateField(label='Дата отправления')
    return_date = forms.DateField(label='Дата возвращения', required=False)
    passengers_count = forms.IntegerField(label='Количество пассажиров', min_value=1)

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = ['image', 'name', 'surname', 'lastname', 'mail']