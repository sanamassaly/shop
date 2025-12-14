from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'slug',
        'created_at',
    ]
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','prix','categorie','disponibilite','quantite_stock','is_featured']
    prepopulated_fields = {'slug': ('name',)}