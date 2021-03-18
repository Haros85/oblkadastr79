from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastral", views.valuation, name="cadastral"),
    path("cadastral/reports", views.reports, name="reports"),
    path("cadastral/acts", views.acts, name="acts"),
]
