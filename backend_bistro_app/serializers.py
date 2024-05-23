from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name
    
    class Meta:
        model = Item
        fields = ['id', 'category_name', 'title', 'description', 'price', 'spiceLevel']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'pickup', 'completed', 'order_items']

class OverOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverOrder
        fields = ['id', 'customer', 'title', 'price']


   # def create(self, validated_data):
       # order_items_data = validated_data.pop