# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:49:22 2018

@author: 21461
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
]