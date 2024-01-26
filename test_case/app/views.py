from django.db import transaction, models
from django.db.models import Sum, Case, When, IntegerField, F, Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Product, Recipe, Ingredient


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    if weight is None:
        return HttpResponse(status=400)

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    Ingredient.objects.update_or_create(recipe=recipe, product=product, defaults={'weight': weight})

    return HttpResponse('Обновлено')


@transaction.atomic
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    with transaction.atomic():
        ingredients = Ingredient.objects.select_for_update().filter(recipe=recipe)
        for ingredient in ingredients:
            ingredient.product.times_used = models.F('times_used') + 1
            ingredient.product.save()

    return HttpResponse('Yeah')


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    recipes = Recipe.objects.annotate(
        total_weight=Sum(
        Case(
            When(ingredient__product=product, then='ingredient__weight'),
            default=0,
            output_field=IntegerField()
                )
            )
        ).filter(Q(total_weight__lt=10) | Q(total_weight=None))

    if not recipes:
        raise Http404('Рецепт не найден')

    return render(request, 'app/recipe.html', {'recipes': recipes})
