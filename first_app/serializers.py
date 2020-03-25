from rest_framework import serializers
from .models import *
import time


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_number = serializers.SerializerMethodField('generate_order_number')
    total_cost = serializers.SerializerMethodField('calculate_cost')
    rate = serializers.SerializerMethodField('fetch_product_rate')

    def generate_order_number(self, instance):
        # latest_order = Order.objects.all().last()
        # serialz = OrderSerializer(latest_order,many=True)
        # print(serialz.data)
        # return instance.id

        year = time.asctime().split(' ')[-1]
        number = '{}/{}/{}'.format('PO', year, instance.id)
        return number

    def calculate_cost(self, instance):
        price = instance.product.cost
        quantity = instance.quantity
        return price * quantity

    def fetch_product_rate(self, instance):
        return instance.product.cost

    class Meta:
        model = Order
        fields = ['company', 'product', 'order_number', 'rate', 'quantity', 'total_cost']
