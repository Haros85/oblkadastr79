from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News, Act


def index(request):
    qs = News.objects.order_by("-pub_date")[:2]
    return render(request, "index.html", {"data": qs})


def valuation(request):
    qs = Act.objects.order_by("-pub_date")[:5]
    return render(request, "valuation.html", {"data": qs})


def acts(request):
    qs = Act.objects.filter(type_act='act').order_by("-pub_date")
    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "acts.html",
        {
            "page": page,
            "paginator": paginator,
        },
    )


def reports(request):
    qs = Act.objects.filter(type_act='report').order_by("-pub_date")
    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "reports.html",
        {
            "page": page,
            "paginator": paginator,
        },
    )