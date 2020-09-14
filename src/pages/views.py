from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    return HttpResponse('<h1>Hello world</h1>')


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact page</h1>')


def about_view(request, *args, **kwargs):
    return HttpResponse('<h1>About page</h1>')


def social_view(request, *args, **kwargs):
    return HttpResponse('<h1>Social page</h1>')
