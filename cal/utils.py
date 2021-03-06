from calendar import HTMLCalendar
from datetime import datetime, timedelta
from .models import Event

class FamilyCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(FamilyCalendar, self).__init__()

    def formatday(self, day, events):
        daily_events = events.filter(start_time__day=day)
        d_events = ''
        for event in daily_events:
            d_events += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class= 'date'>{day}</span><ul> {d_events} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for dayz, week_day in theweek:
            week += self.formatday(dayz, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal