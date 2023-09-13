from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

class restAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer