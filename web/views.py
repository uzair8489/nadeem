from django.shortcuts import render
from .models import *
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
import requests

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def services(request):
    return render(request, 'services.html')

# Login Module 
def login(request):
    if request.user.is_authenticated:
            return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def blogs(request):
    return render(request, 'blogs.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        # image = request.FILES['img']
        if len(password1) < 8:
             messages.info(request,'Your password must be 8 character long.')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
            elif user_data.objects.filter(contact=phone).exists():
                messages.info(request,'Phone number linked with another account')
            else:
                user = User.objects.create_user(first_name=first_name, last_name = last_name, username = username, email = email, password = password1)
                user.save()
                print(user.id)
                user_d = user_data(id = user.id, contact = phone, address = address)
                user_d.save()
                message  = 'Your account has been created successfully. You can login in now using your credentials. Thanks for joining us.'
                ema= 'skindcs22@gmail.com'
                em = EmailMessage(
                    'Account Created Successfully',
                    message,
                    settings.EMAIL_HOST_USER,
                    [ema],
                )
                em.send()
                return redirect('login')


        else:
            print('password not matching...')
        return redirect('signup')

    else:
        return render(request, 'user_signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')