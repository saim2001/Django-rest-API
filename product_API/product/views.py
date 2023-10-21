from rest_framework.response import Response

from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerialize

# Create your views here.
class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize

class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ListProductsByCategory(generics.ListAPIView):

    serializer_class = ProductSerialize

    def get_queryset(self):
        category = self.kwargs["category"]
        return Product.objects.filter(category=category)
    
class ListProductsByStock(generics.ListAPIView):

    serializer_class = ProductSerialize

    def get_queryset(self):

        order = self.kwargs["order"]
        if order == "asc":
            return Product.objects.order_by("stock")
        elif order == "desc":
            return Product.objects.order_by("-stock")
        else:
            return Product.objects.all()
        
class ListProductsByPrice(generics.ListAPIView):

    serializer_class = ProductSerialize

    def get_queryset(self):

        order = self.kwargs["order"]
        if order == "asc":
            return Product.objects.order_by("price")
        elif order == "desc":
            return Product.objects.order_by("-price")
        else:
            return Product.objects.all()
    