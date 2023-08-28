from django.contrib import admin
from .models import Article, Author

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'date_updated')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'first_name', 'last_name')