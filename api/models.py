from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    category = models.ForeignKey(Category,null = True,blank = True,on_delete = models.SET_NULL)
    available = models.BooleanField(default = True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add = True)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)

    def __str__(self):
        return f'Cart {self.id}'

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Product,through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_shipped = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"order id:{self.id},user:{self.user}"

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
