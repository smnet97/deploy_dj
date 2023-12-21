from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='product/')
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
