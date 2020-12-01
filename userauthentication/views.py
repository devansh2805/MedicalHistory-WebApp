from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import AdditionalUserInformation
import random, string

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            userType = form.cleaned_data.get('userType')
            addUserInfo(username, int(userType))
            messages.success(request, 'Account Created Successfully for ' + str(username))
            return redirect('login')
    context = {'form': form}
    return render(request, 'userauthentication/register.html', context=context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is Incorrect!')
    context = {}
    return render(request, 'userauthentication/login.html', context=context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def addUserInfo(username, userType):
    userInfo = AdditionalUserInformation()
    userInfo.username = username
    userInfo.userId = generateUserId()
    userInfo.userType = userType
    userInfo.save()

def generateUserId():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(6))