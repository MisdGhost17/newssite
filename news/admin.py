from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug":('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published')
    readonly_fields = ('time_create', 'get_html_photo',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.title = 'Админ-панель newstoday'
admin.site.site_header = 'Админ-панель newstoday'
