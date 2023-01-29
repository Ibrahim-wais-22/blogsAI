from django.contrib import admin
from .models import Post, Author, Category, Tag

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name', 'email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('pub_date', 'author')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    filter_horizontal = ('categories', 'tag')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Tag)
