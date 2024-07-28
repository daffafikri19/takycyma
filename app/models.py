from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title

class Page(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
