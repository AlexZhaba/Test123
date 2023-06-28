from django.contrib import admin

# Register your models here.
from shop.models import Category, Product, Review, Specification, ProductSpecification, Image

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Specification)
admin.site.register(ProductSpecification)
admin.site.register(Image)
