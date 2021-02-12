from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    @property
    def get_html_url(self):
        url = reverse('cal:edit_event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'