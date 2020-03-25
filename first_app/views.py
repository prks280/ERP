from django.shortcuts import render
from rest_framework import viewsets

from .models import Company, Product, Order
from .serializers import CompanySerializer, ProductSerializer, OrderSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def get_queryset(self):
    #     print(1)
    #     return Order.objects.filter(product = Product.objects.filter(company = self.company))
