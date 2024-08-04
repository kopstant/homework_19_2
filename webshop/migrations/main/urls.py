from django.urls import path

from webshop import admin
from webshop.apps import WebshopConfig

app_name = WebshopConfig.name

urlpatterns = [
    path('',)
]