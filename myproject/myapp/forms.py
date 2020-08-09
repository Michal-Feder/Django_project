from django import forms
from django.forms import DateInput


class DateDateField(forms.DateField):
    input_type = 'date'


class DateForm(forms.Form):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), label='Date: ')

class A:
    result=''
    month=''