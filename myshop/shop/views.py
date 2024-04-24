from typing import Any
from .models import Category, Product
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView



class ProductList(TemplateView):
    TAG = ['ProductList']
    template_name = 'shop/product/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(available=True)

        if category_slug:
            context['category'] = get_object_or_404(Category, slug=category_slug)
            context['products'] = context['products'].filter(category=context['category'])
        
        return context
    

class ProductDetail(TemplateView):
    TAG = ['ProductDetail']
    template_name = 'shop/product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        context['product'] = get_object_or_404(Product,
                                               id=id,
                                               slug=slug,
                                               available=True)
        return context