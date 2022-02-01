# -*- coding: utf-8 -*-

from django.urls import *
from currencies.views import set_currency

urlpatterns = [
    re_path(r'^setcurrency/$', set_currency, name='currencies_set_currency'),
]
