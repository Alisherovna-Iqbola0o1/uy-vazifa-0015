from django.contrib import admin
from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)   # <-- tuple bo'lishi kerak

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price', 'stock', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'stock')



