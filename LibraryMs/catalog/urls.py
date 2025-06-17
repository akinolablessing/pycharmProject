from django.urls import path, include
from . import views


urlpatterns = [
    path('books', views.get_books),

    path("greet/<name>",views.greet),
]