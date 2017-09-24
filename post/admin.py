from django.contrib import admin

from .models import Post, Comment

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('post', 'text')
