from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'slug', 'description',
                  'prix', 'categorie', 'disponibilite',
                  'quantite_stock', 'is_featured'
                  ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nom du produit'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'slug-produit'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description du produit', 'row':5}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix du produit', 'step':0.01}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'disponibilite': forms.Select(attrs={'class': 'form-control'}),
            'quantite_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0', 'min': 0}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'})

        }

        labels = {
            'name': 'Nom du produits',
            'slug': 'Slug',
            'description': 'Description',
            'prix': 'Prix (FCFA)',
            'categorie': 'Catégorie',
            'disponibilite':'Dsiponibilité',
            'quantite_stock': 'Quantité en stock',
            'image': 'Imager du produit',
            'is_featured': 'En vedette'
        }

