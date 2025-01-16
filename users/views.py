from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm

def register_view(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                form.save()  # Save the user to the database
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    messages.success(request, f'Account created for {username}!')
                    return redirect('ki-tech-home')
    else:
        return redirect('ki-tech-home')
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def login_view(req):
    error_msg = ""  # Initialize error_msg to avoid NameError
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password1')
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req, f'Logged In Successfully !')
            return redirect('ki-tech-home')
        else:
            error_msg = "Invalid Credentials!"
    return render(req, 'users/login.html', {'error': error_msg})



def logout_view(req):
    if req.method == "POST":
        logout(req)
        return redirect('login')
    else:
        return redirect('ki-tech-home')