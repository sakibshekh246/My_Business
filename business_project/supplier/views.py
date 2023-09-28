# supplier/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})

# Add more views as needed (e.g., create, update, delete)

