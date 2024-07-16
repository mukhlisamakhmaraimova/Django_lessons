# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
#
# class CustomUserCreationForm(UserCreationForm):
#     # Meta -> asosiy classiga qoshimcha qlsh degani
#     class Mete(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'first_name', 'last_name', 'email', 'age')
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'first_name', 'last_name', 'email',  'age')




from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)