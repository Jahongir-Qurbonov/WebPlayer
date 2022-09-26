from django.shortcuts import render
from django.http import HttpRequest
from .models import Song

# Create your views here.

def songs_player(request: HttpRequest):
    songs = Song.objects.all()
    context_songs = []
    for i, song in enumerate(songs, start=1):
        context_songs.append({
            'id': i,
            'title': song.title,
            'artist': song.artist,
            'album': song.album,
            'genre': song.genre,
            'audio_file': song.audio_file[:song.audio_file.rfind('.')],
        })

    context = {
        'songs': context_songs,
    }

    return render(request, template_name='player/songs_player.html', context=context)