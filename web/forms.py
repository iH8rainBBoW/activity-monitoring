from django.forms import ModelForm
from django.db import models
from django.db.models import Model
from django.conf import settings
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input-field", 'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"input-field", 'placeholder':'Пароль', 'type':'password'}))


