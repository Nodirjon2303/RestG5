from django.db import models
from rest_framework.authtoken.admin import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    shelf_time = models.DateField(null=True)
    shtrix = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Stock(models.Model):
    products1 = models.ManyToManyField(Product, related_name='Stock1')
    products2 = models.ManyToManyField(Product, related_name='Stock2')
    description = models.TextField(null=True)
    # def __str__(self):
    #     return self.name


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    changed_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.product.name


class Supplier(models.Model):
    required_name = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.required_name


class Debit(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=1)
    # def __str__(self):
    #     return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    required_name = models.CharField(max_length=50)


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    sale_date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        sp = SaleProduct.objects.filter(sale = self)
        return sum([s.summa for s in sp])
class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField(default=1)
    sold_price = models.FloatField(null=True)

    @property
    def set_price(self):
        self.sold_price = self.product.price
    @property
    def summa(self):
        return self.product.price*self.quantity



