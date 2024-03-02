from django.contrib import admin
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'steps', 'time_minutes', 'image', 'author', 'category',)
    list_display = ('id', 'title', 'author', 'category_title',)
    list_filter = ('category',)
    search_fields = ('title', 'author',)
    ordering = ('title',)
    raw_id_fields = ('author', 'category',)
