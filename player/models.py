from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
    album = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    audio_file = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return str(self.audio_file)
