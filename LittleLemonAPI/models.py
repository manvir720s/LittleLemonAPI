from django.db import models
# Assuming you are using Django's built-in User model
from django.contrib.auth.models import User

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(
        MenuItem, related_name='carts', blank=True)

    # Method to clear menu_items
    def clear_menu_items(self):
        self.menu_items.clear()


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer_orders')
    delivery_crew = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='crew_orders', null=True, blank=True,)
    items = models.ManyToManyField(MenuItem)
    status = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
