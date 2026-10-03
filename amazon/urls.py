from django.urls import path  # type: ignore[import-not-found]
from amazon import views

urlpatterns = [
    path("", views.home, name="home"),
]