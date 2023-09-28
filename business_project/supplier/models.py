# supplier/models.py
from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    other_details = models.CharField(max_length=40)

    def __str__(self):
        return self.name

