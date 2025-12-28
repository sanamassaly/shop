from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Category, Product
from . forms import ProductForm


class ProduitListViews(ListView):
    model = Product
    template_name = 'produit_list.html'
    context_object_name = 'produits'

    def get_queryset(self):
        return Product.objects.all()


class ProduitDetail(DetailView):
    model = Product
    template_name = 'produit_detail.html'
    context_object_name = 'produit'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

   #def get_object(self, queryset=None):
        #return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Voir les produits similaire de la meme categorie
        context['related_produits'] = Product.objects.filter(categorie=self.object.categorie).exclude(id=self.object.id)[:5]

        return context


class ProduitCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    login_url = '/admin/login'

    def form_valid(self, form):
        messages.success(self.request, 'Produit cree avec succés!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Erreur lors de la creation du produit.')
        return super().form_valid(form)


class ProduitUpdateViews(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    login_url = '/admin/login'
    success_url = reverse_lazy('product:list_produit')

    def form_valid(self, form):
        messages.success(self.request, 'Produit modifié avec succés!')
        return super().form_valid(form)