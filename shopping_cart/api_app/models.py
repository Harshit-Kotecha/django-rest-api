from django.db import models


class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField(default=0, null=False)
    product_quantity = models.IntegerField(default=1)
