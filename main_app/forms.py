from django import forms
from .models import Date

class DateForm(forms.ModelForm):
  class Meta:
    model = Date
    fields = ['day']
    widgets = {
      'day': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={
          'placeholder': 'Select a date',
          'type': 'date'
        }
      ),
    }
