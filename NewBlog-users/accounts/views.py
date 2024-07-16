# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .forms import CustomUserCreationForm
#
# # Create your views here.
#
# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'




from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

