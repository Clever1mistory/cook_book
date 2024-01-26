from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    times_used = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    products = models.ManyToManyField(Product, through='Ingredient')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        unique_together = ('product', 'recipe')

    def __str__(self):
        return f'{self.product.name} - {self.weight}'
