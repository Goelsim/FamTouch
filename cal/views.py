from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from .utils import FamilyCalendar
from .models import *
# Create your views here.

class FamCalendar(generic.ListView):
    model = Event
    template_name = 'cal/famcal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = FamilyCalendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context
    
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
    