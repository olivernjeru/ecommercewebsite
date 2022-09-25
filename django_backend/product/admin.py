from django.contrib import admin

from .models import Category, Product

# Models created are registered here so that they appear on the admin page
# Category Model is registered below
admin.site.register(Category)
# Product Model is registered below
admin.site.register(Product)
