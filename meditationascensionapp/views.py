from django.http import HttpResponse
from django.shortcuts import render
from .models import Testimonial


def index(request):
    return render(request, 'meditationascensionapp/index.html')


def about(request):
    return render(request, 'meditationascensionapp/about.html')


def events(request):
    return render(request, 'meditationascensionapp/events.html')


def testimonials(request):
    all_testimonials = Testimonial.objects.all()
    context = {
        'all_testimonials': all_testimonials,
    }
    return render(request, 'meditationascensionapp/testimonials.html', context)


def blog(request):
    return render(request, 'meditationascensionapp/blog.html')


def contact(request):
    return render(request, 'meditationascensionapp/contact.html')