from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateBook(ModelForm):
    class Meta:
        model=LibBook
        fields='__all__'

class CreateCat(ModelForm):
    class Meta:
        model=LibCategory
        fields='__all__'

class CreateOrde(ModelForm):
    class Meta:
        model=LibBookAcquired
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomerForm(ModelForm):
    class Meta:
        model=LibUser
        fields='__all__'
        exclude=['user']