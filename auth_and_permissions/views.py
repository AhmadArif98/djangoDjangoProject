from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        User = get_user_model()
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponseRedirect('/login')


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'login.html')

def signin_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username, '', password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')