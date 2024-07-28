from django.db import models
import os


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    volumes = models.IntegerField()
    synopsis = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name="chapters", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="chapters/covers/", blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.manga.title} - {self.title}"


def chapter_images_path(instance, filename):
    return os.path.join(
        "mangas", instance.chapter.manga.title, instance.chapter.title, filename
    )


class MangaPanels(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='panels', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to=chapter_images_path)

    def __str__(self):
        return f"Image {self.id} from {self.chapter}"
