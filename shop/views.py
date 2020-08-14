from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
# view to list products
def product_list(request, category_slug=None):
    Category = None
    categories =  Category.objects.all()
    if category_slug:
        Category = get_object_or_404(Category, slug=category-slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',{'category': category,'categories': categories, 'products': products} )

# view to list a single product
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html',{'product': product})