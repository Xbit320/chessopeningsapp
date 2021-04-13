from django.contrib import admin
from .models import Opening, Categories, CategoriesTypes

# Register your models here.

admin.site.register(Opening)
admin.site.register(Categories)
admin.site.register(CategoriesTypes)
