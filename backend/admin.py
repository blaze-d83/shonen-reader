from django.contrib import admin
from .models import Manga, Chapter, Genre, MangaPanels

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date')
    search_fields = ('title', 'author')

class MangaPanelsInline(admin.TabularInline):
    model = MangaPanels
    extra = 1

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'manga', 'release_date')
    search_fields = ('title', 'manga_title')
    list_filter = ('manga',)
    inlines = [MangaPanelsInline]

@admin.register(MangaPanels)
class MangaPanelsAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'image')
    search_fields = ('chapter__title', 'chapter__manga__title')
    list_filter = ('chapter__manga',)
    
