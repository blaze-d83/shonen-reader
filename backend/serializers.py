from rest_framework import serializers
from .models import Genre, Manga, Chapter, MangaPanels

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class MangaPanelSerializers(serializers.ModelSerializer):
    class Meta:
        model = MangaPanels 
        fields = '__all__'
