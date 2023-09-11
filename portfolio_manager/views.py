from django.shortcuts import render
from django.shortcuts import redirect
from .models import Portfolio
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate


def home(request):
    return render(request, "home.html")


def portfolio(request):
    portfolio = Portfolio.objects.first()
    return render(request, "portfolio.html", {"portfolio": portfolio})


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign-up.html", {"form": form})
