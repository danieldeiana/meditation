from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    pass


admin.site.register(Testimonial, TestimonialAdmin)
