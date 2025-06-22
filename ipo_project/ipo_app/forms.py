from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import IPO

class IPOForm(forms.ModelForm):
    class Meta:
        model = IPO
        fields = '__all__'
        widgets = {
            'opening_date': forms.DateInput(attrs={'type': 'date'}),
            'closing_date': forms.DateInput(attrs={'type': 'date'}),
            'listing_date': forms.DateInput(attrs={'type': 'date'}),
        }    

    def clean(self):
        cleaned_data = super().clean()
        opening_date = cleaned_data.get('opening_date')
        closing_date = cleaned_data.get('closing_date')
        listing_date = cleaned_data.get('listing_date')

        if opening_date and closing_date:
            if closing_date < opening_date:
                raise ValidationError("❌ Closing date cannot be before opening date.")
            elif opening_date < date.today():
                raise ValidationError("❌ Opening date cannot be in the past.") 
            elif listing_date < closing_date:
                raise ValidationError("❌ Listing date cannot be before closing date.")
            elif closing_date == opening_date:
                raise ValidationError("❌ Closing date cannot be same as opening date.")