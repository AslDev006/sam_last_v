from django import forms
from django.core.exceptions import ValidationError
import re

class MyForm(forms.Form):
    name = forms.CharField(
        label='Ism',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ismingizni kiriting'})
    )
    phone_number = forms.CharField(
        label='Telefon raqam',
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Telefon raqamingizni kiriting'})
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Telefon raqami formatini tekshirish
        if not re.match(r'^\+?\d{9,15}$', phone_number):
            raise ValidationError('Telefon raqami to\'g\'ri formatda emas. (masalan: +998901234567)')
        return phone_number