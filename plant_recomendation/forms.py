# forms.py
from decimal import Decimal
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class DataForm(forms.Form):
    altitude = forms.DecimalField(
        max_digits=5, decimal_places=1, label='Ketinggian di atas permukaan laut (mdpl)',
        validators=[MinValueValidator(500), MaxValueValidator(1310)]
    )
    temperature = forms.DecimalField(
        max_digits=3, decimal_places=1, label='Temperatur (°C)',
        validators=[MinValueValidator(0.5), MaxValueValidator(12.5)]
    )

    def clean_altitude(self):
        altitude = self.cleaned_data['altitude']
        if not (500 <= altitude <= 1310):
            raise forms.ValidationError(
                "Ketinggian di atas permukaan laut harus berada antara 500 hingga 1310.")
        return altitude

    def clean_temperature(self):
        temperature = self.cleaned_data['temperature']
        if not (1 <= temperature <= 12.5):
            raise forms.ValidationError(
                "Temperatur harus berada antara 1 hingga 12.5")
        return temperature
