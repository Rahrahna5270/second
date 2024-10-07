from django.db import models
from django.contrib.auth.models import User
class category(models.Model):
    name=models.CharField(max_length=200)
    image=models.FileField(upload_to='products/images')
    def __str__(self):
        return self.name
    

# Create your models here.
class product(models.Model):
    Category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    rate=models.IntegerField()
    image=models.FileField(upload_to='products/images')
    description=models.TextField()
    # fabric=models.TextField()
    # style=models.TextField()
    # fittype=models.TextField()
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    totals=models.IntegerField(default=1)
    rate=models.IntegerField(default=1)
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    # def total_price(self):
    #     return sum(i.item_price() for i in self.Cartitem.set.all())
    # def __str__(self):
    #     return f"{self.quantity} x {self.product.name}"
    # def item_price(self):
    #     return self.quantity * self.product.rate 
    
# class Cartitem(models.Model):
#     cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"
#     def item_price(self):
#         return self.quantity * self.product.rate 

    

   
    
