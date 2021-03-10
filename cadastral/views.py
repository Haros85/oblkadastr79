from django.shortcuts import render, redirect

from .models import News, Act


def index(request):
    qs = News.objects.order_by("-pub_date")[:2]
    return render(request, "index.html", {"data": qs})


def valuation(request):
    qs = Act.objects.order_by("-pub_date")[:5]
    return render(request, "valuation.html", {"data": qs})