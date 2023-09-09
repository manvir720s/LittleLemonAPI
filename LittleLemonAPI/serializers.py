from rest_framework import serializers
from .models import MenuItem, Cart, Order
from django.contrib.auth.models import User


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'email']


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    # This includes the MenuItems using their serializer
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['user', 'menu_items']


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer
    delivery_crew = UserSerializer
    # This includes the MenuItems using their serializer
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'delivery_crew', 'items']
