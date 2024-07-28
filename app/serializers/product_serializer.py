from rest_framework import serializers
from ..models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()

    def get_pictures(self, obj):
        first_image = obj.pictures.first()
        if first_image:
            return first_image.image.url
        return None

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'link', 'pictures']
