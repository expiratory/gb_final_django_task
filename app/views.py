import random

from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import RecipeForm
from .models import Recipe
from .forms import UserRegistrationForm


def index(request):
    all_recipies_ids = Recipe.objects.all().values_list('id', flat=True)

    if len(all_recipies_ids) >= 5:
        random_recipes_ids = random.sample(list(all_recipies_ids), min(5, len(all_recipies_ids)))
        recipes = Recipe.objects.filter(id__in=random_recipes_ids)
    else:
        recipes = Recipe.objects.all()

    context = {
        'page_title': 'Главная страница',
        'recipies': recipes
    }
    return render(request, 'index.html', context=context)


def retrieve_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {
        'page_title': recipe.title,
        'recipe': recipe
    }
    if request.user == recipe.author:
        if request.method == 'POST':
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('recipe_success_page')
        else:
            form = RecipeForm(instance=recipe)
            context['form'] = form
    return render(request, 'retrieve_recipe.html', context=context)


def recipies(request):
    recipies = Recipe.objects.all()
    context = {
        'page_title': 'Все рецепты',
        'recipies': recipies
    }
    return render(request, 'recipies.html', context=context)


def add_recipe(request):
    if isinstance(request.user, AnonymousUser):
        context = {
            'page_title': 'Error',
            'error': '403 Forbidden'
        }
        return render(request, 'error.html', context=context)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_success_page')
    else:
        form = RecipeForm()
    context = {
        'page_title': 'Добавление рецепта',
        'form': form
    }
    return render(request, 'add_recipe.html', context=context)


class CreateUserView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = '/login/'
