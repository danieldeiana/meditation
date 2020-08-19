from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MailListForm
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MailListForm()
    return render(request, 'meditationascensionapp/contact.html', {'form': form})
