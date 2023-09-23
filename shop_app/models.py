from django.db import models
from django.contrib.auth.models import User

# Create your models here.    

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=45,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images')

    CATEGORY_CHOICES = [
        ('Men', 'men'),
        ('Women', 'women'),
        ('Accessories', 'accessories'),
        ('Shoes', 'shoes'),
        ('Watches', 'watches'),
        ('Bag', 'bag'),
        
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    
class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'color', 'size')

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    productv = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)  # product model
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x ({self.productv.product.name}) in Cart of {self.user.first_name} {self.user.last_name}"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Linked products

    def __str__(self):
        return self.product.name
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + self.city
    
class orderedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + str(self.date)[:10]
    
class Feedback(models.Model):
    cust_email = models.EmailField()
    message = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.cust_email + ' ' + str(self.date)