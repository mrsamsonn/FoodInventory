from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'ean', 'title', 'brand')  # Fields to display in the admin list view
    search_fields = ('upc', 'title', 'brand')  # Fields to enable search in the admin
    list_filter = ('brand',)  # Filters to enable filtering in the admin
