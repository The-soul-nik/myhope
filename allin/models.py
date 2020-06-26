from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title


class God(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
