from django.shortcuts import render
from .models import Portfolio


def home(request):
    return render(request, "home.html")


def portfolio(request):
    portfolio = Portfolio.objects.first()
    return render(request, "portfolio.html", {"portfolio": portfolio})
