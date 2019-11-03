from django.shortcuts import render, HttpResponse
from . import models
from django.views import generic

# Create your views here.


def home(request):
    return render(request, "home.html")


def all(request):
    model = models.Blog
    context = {
        "blog": model
    }
    return render(request, "all_blogs.html", context)


def bloggers(request):
    return HttpResponse("Func bloggers")
