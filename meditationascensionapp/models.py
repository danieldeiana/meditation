from django.db import models


class Testimonial(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)
