from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    price = models.IntegerField()

    category = models.CharField(max_length=100)

    exchange = models.BooleanField(default=False)

    image = models.ImageField(
        upload_to='products/',
        default='products/default.jpg'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class ExchangeRequest(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    offered_product = models.CharField(
        max_length=200,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    condition = models.CharField(
        max_length=100,
        blank=True
    )

    exchange_image = models.ImageField(
        upload_to='exchange/',
        blank=True,
        null=True
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.requester.username