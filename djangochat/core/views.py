from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SignUpForm

def index(request):
    return render(request, "core/index.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = SignUpForm
    return render(request, "core/signup.html", {"form":form})

def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("index")
    return HttpResponse("Not allowed", status=405)

