from django.db import models
from embed_video.fields import EmbedVideoField


class Item(models.Model):
    name = models.CharField('Video name', max_length=100, null=True)
    video = models.URLField()  # same like models.URLField()

    def __str__(self):
        return self.name