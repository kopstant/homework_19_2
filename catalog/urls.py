from django.urls import path

from catalog import admin
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('',)
]
