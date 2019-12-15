import uuid
from django.db import models
from django.conf import settings


class Item(models.Model):
    CATEGORY_CHOICES = (
        ("DRESSES", "Dresses"),
        ("SWEATERS", "Sweaters"),
        ("JACKETS", "Jackets"),
        ("BLOUSES", "Blouses"),
        ("SHORTS", "Shorts"),
        ("SKIRTS", "Skirts"),
        ("PANTS", "Pants"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items', null=True, blank=True)
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.PositiveSmallIntegerField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    ship_to = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order} - {self.item} - {self.amount}"

