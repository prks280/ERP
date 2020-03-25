from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    gst = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return 'name :{}, gst :{}'.format(self.name, self.gst)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cost = models.FloatField(default=0.0)

    def __str__(self):
        return 'name :{}, company :{}, cost :{}'.format(self.name, self.company.name, self.cost)


class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return 'company :{}, product :{}, quantity :{}'.format(self.company.name, self.product.name, self.quantity)
