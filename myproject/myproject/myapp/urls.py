# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views
urlpatterns = [#patterns('myproject.myapp.views',
    url(r'^index/$', views.index , name='index'),
]
