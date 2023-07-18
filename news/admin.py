from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(News)