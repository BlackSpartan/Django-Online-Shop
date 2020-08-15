from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # a foreign key to the category model
    name = models.CharField(max_length=200, db_index=True) # the name of the product
    slug = models.SlugField(max_length=200, db_index=True) # The slug for this product to build beautiful URLs.
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # An optional product image.
    description = models.TextField(blank=True)  # An optional description of the product.
    price = models.DecimalField(max_digits=10, decimal_places=2) # variable to store float price 
    available = models.BooleanField(default=True) # A Boolean value that indicates whether the product is available or not. It will be used to enable/disable the product in the catalog.
    created = models.DateTimeField(auto_now_add=True) # This field stores when the object was created.
    updated = models.DateTimeField(auto_now=True) # This field stores when the object was last updated.

    class Meta:
        ordering = ('name',)

        index_together = (('id', 'slug'),)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

