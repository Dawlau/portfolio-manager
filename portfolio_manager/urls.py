from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("sign-up", views.sign_up, name="sign-up"),
]
