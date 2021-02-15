from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    #url('', views.index, name='index'),
    url('', views.FamCalendar.as_view(), name='famcal'),
    url('admin/cal/event/add/', views.event, name='new_event'),
    url('admin/cal/event/(?P<event_id>\d+)/change/edit/', views.event, name='edit_event'),
]