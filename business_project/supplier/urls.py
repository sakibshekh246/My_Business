# supplier/urls.py
from django.urls import path
from . import views

app_name = 'supplier'

urlpatterns = [
    path('', views.supplier_list, name='supplier-list'),
    # Add more URL patterns as needed
]
