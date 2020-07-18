from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at meditation index.")


def about(request):
    return HttpResponse("Hello, world. You're at meditation about.")


def events(request):
    return HttpResponse("Hello, world. You're at meditation programs and events.")


def testimonials(request):
    return HttpResponse("Hello, world. You're at meditation testimonials.")


def blog(request):
    return HttpResponse("Hello, world. You're at meditation blog.")


def contact(request):
    return HttpResponse("Hello, world. You're at meditation contact.")