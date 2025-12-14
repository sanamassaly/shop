from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', ProduitListViews.as_view(), name='list_produit'),
    path('mesproduit/<str:slug>', ProduitDetail.as_view(), name='detail'),
    path('add', ProduitCreateView.as_view(), name='add_product')
]
