from rest_framework import generics
from .models import Genre, Manga, Chapter, MangaPanels
from .serializers import (
    GenreSerializer,
    MangaSerializer,
    ChapterSerializers,
    MangaPanelSerializers,
)


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MangaList(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer


class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer


class ChapterList(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers


class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'chapter_pk'


class MangaPanelsList(generics.ListCreateAPIView):
    queryset = MangaPanels.objects.all()
    serializer_class = MangaPanelSerializers


class MangaPanelsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MangaPanels.objects.all()
    serializer_class = MangaPanelSerializers
