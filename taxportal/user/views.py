from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout


def home(request):
    return render(request, 'user/index.html')


def about(request):
    return render(request, 'user/about.html')


def register(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Your Account is successfully created")
        return redirect('/login')
    return render(request, 'user/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'user/home.html')

        else:
            messages.error(request, "Invalid user")
            return redirect('')

    return render(request, 'user\login.html')


def signout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('')
