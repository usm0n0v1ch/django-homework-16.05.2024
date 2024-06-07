from django.contrib import admin

from myapp.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Article, ArticleAdmin)

