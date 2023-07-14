from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ("title", )}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')
    fields = ('title', 'slug', 'description', 'category', 'image', 'author')
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
