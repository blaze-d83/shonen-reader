from django.urls import path

from backend.views import (
    ChapterDetail,
    ChapterList,
    GenreDetail,
    GenreList,
    MangaDetail,
    MangaList,
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("mangas/", MangaList.as_view(), name="manga-list"),
    path("mangas/<int:pk>", MangaDetail.as_view(), name="manga-detail"),
    path("mangas/<int:manga_pk>/chapters/", ChapterList.as_view(), name="chapter-list"),
    path("mangas/<int:manga_pk>/chapters/<int:chapter_pk>", ChapterDetail.as_view(), name="chapter-detail"),
]
