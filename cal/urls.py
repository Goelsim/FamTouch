from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    #url('', views.index, name='index'),
    url('', views.FamCalendar.as_view(), name='famcal'),
    url('event/new', views.event, name='new_event'),
    url('event/edit/(?P<event_id>\d+)/', views.event, name='edit_event'),
]