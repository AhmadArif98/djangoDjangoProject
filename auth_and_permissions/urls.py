from django.contrib import admin
from django.urls import path
from auth_and_permissions import views

# admin    admin
# user1    user***123
# user2    user***456
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_user, name='login'),
    path('signin', views.signin_user, name='signin'),
    path('logout', views.logout_user, name='logout'),

]