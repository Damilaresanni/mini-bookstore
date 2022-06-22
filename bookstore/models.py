from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    Author = models.CharField(max_length=200, null=True)
    published_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    quantity = models.IntergerField(default=0, null= True)

class ShippingAddress(models.Model):
        order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
        book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
        address= models.CharField(max_length=200, null=True)
        city = models.CharField(max_length=200, null=True)
        state = models.CharField(max_length=200, null=True)
        date_added = models.DateTimeField(auto_now_add =True, null=True)

        def __str__(self):
            return self.address
