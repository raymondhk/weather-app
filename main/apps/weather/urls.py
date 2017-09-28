from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process1$', views.newLocation1),
    url(r'^process2$', views.newLocation2),
    url(r'^process3$', views.newLocation3),
    url(r'^process4$', views.newLocation4),
]
