from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('', views.RegisterView.as_view(), name='register'),
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
