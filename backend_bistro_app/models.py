from django.db import models

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2) # price format
    spiceLevel = models.IntegerField(choices=[(i, i) for i in range(1,5)]) # spice level 1 - 4

class Customer(models.Model):
    name = models.TextField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pickup = models.DateTimeField()
    completed = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

