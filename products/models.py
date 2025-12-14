from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank = True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'Categorie'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product (models.Model):
    DISPONIBILTE = (
        ('en_stock', 'En stock'),
        ('en_rupture_de_stock', 'En rupture de stock'),
        ('precommande', 'Precommande')
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produits')
    disponibilite = models.CharField(max_length=20, choices=DISPONIBILTE, default='en_stock')
    quantite_stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Produit'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug':self.slug})

    @property
    def est_dispo(self):
        return self.disponibilite == 'disponibilite' and self.quantite_stock > 0