from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'slug', 'description', 'prix', 'categorie', 'disponibilite', 'quantite_stock', 'is_featured']
