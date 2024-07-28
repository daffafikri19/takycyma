from django.contrib import admin
from .models import Product, ProductImage, Banner, Page

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'link')
    search_fields = ('title',)
    list_filter = ('price',)

    class ProductImageInline(admin.TabularInline):
        model = ProductImage
        extra = 1

    inlines = [ProductImageInline]

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)