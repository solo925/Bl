from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_field = ('title','body')
    prepopulated_field = {'slug':('title',)}
    raw_id_field = ('author',)
    date_hierachy = 'publish'
    ordering = ('status','publish')