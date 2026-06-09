from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            role = form.cleaned_data.get('role')

            group, created = Group.objects.get_or_create(name=role.capitalize())
            user.groups.add(group)

            messages.success(request, "Registration successfull! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Please Enter valid credentials")
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('article_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')



