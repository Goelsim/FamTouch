from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url('', views.index, name='index'),
]