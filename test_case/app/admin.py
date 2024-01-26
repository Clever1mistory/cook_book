from django.contrib import admin
from .models import Product, Recipe, Ingredient


class IngredientAdmin(admin.TabularInline):
    model = Ingredient
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'times_used']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [IngredientAdmin]


admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)


