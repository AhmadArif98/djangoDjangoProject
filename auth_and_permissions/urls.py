from django.contrib import admin
from django.urls import path
from auth_and_permissions import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_user, name='login'),
    path('signin', views.signin_user, name='signin'),
    path('logout', views.logout_user, name='logout'),

]