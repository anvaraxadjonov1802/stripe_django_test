from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ("usd", "USD"),
        ("eur", "EUR"),
        ("uzs", "UZS"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default="usd",
    )
    image = models.ImageField(upload_to="items/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency.upper()}"