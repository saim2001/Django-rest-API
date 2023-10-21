from .models import Product
from rest_framework import serializers


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



