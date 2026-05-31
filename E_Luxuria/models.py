from django.db import models
# class Log(models.Model):
#     email= models.CharField(max_length=200)
#     psw= models.CharField(max_length=100)
    # Create your models here.

class Register(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    Password= models.CharField(max_length=100)
    Confirm_Password= models.CharField(max_length=100)
    Mobile_No= models.CharField(max_length=12)
    Address= models.CharField(max_length=200)
    Gender= models.CharField(max_length=10)
    Country= models.CharField(max_length=100)
    State= models.CharField(max_length=100)
    PIN= models.CharField(max_length=50)
    status = models.IntegerField(default=1)
class Product(models.Model):
    productname=models.CharField(max_length=100)
    product_img=models.ImageField(upload_to="product/")
    product_price=models.IntegerField()
    product_oprice=models.IntegerField()
    product_quantity=models.IntegerField()
    product_dprice=models.IntegerField()
    product_description=models.TextField()
    product_gst=models.IntegerField()
    status=models.IntegerField(default=1)
    added_on=models.DateField(auto_now=True)
class Cart(models.Model):
    pid=models.IntegerField()
    uid=models.IntegerField()
    qty=models.IntegerField()
    status=models.IntegerField(default=1)
    added_on=models.DateField(auto_now=True)