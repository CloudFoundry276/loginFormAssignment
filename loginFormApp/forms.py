from django import forms
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,
                               validators=[validators.MinLengthValidator(8),
                                           validators.MaxLengthValidator(20)])
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[validators.MinLengthValidator(8),
                                           validators.MaxLengthValidator(16)])
