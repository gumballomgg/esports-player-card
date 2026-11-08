from django.shortcuts import render


def home(request):
    """PG-01. Главная страница."""
    return render(request, "web/home.html")
