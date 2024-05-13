from django.contrib import admin
from recipe.models import Recipe
from recipe.models import Review

# Register your models here.

admin.site.register(Recipe)

admin.site.register(Review)