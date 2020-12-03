from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import View

from throttle.decorators import throttle
#https://github.com/sobotklp/django-throttle-requests

from .models import UserDetail
from .forms import UserDetailForm

class RegisterView(View):

    @throttle(zone='default')
    def get(self, request):
        if len(request.user.username):
            return redirect(reverse('login'))

        return render(request, 'register.html', { 'form': UserCreationForm() })
    
    @throttle(zone='default')
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, 'register.html', { 'form': form })

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        instance = None
        if hasattr(request.user, 'userdetail'):
        	instance = request.user.userdetail
        form = UserDetailForm(instance=instance)
        return render(request, 'profile.html', { 'form': form })

    def post(self, request):
        instance = UserDetail.objects.filter(user=request.user).first()
        form = UserDetailForm(request.POST, instance=instance or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse('profile'))
        else:
            return render(request, 'profile.html', {'form': form})