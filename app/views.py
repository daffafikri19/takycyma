from django.shortcuts import render
from .models import Product
from .serializers.product_serializer import ProductSerializer

def homepage(request):
    datasrc = Product.objects.all()
    serializer = ProductSerializer(datasrc, many=True)
    products = serializer.data

    context = {
        'products': products
    }
    return render(request, 'site/index.html', context)
