from django.contrib import admin
from django.utils.safestring import mark_safe

<<<<<<< HEAD
from .models import Articles
=======
from book.models import Articles
>>>>>>> e1673953bd0779a3a8143234054b5b49b995eb9b


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
<<<<<<< HEAD
=======
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
>>>>>>> e1673953bd0779a3a8143234054b5b49b995eb9b
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


admin.site.register(Articles, ArticlesAdmin)
