from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to="shop/")
    stuck_keeping_unit = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True
    )  # sku

    def __str__(self):
        return f"{self.name} - {self.category}"



