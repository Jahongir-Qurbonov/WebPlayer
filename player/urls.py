from django.urls import path
from .views import songs_player

urlpatterns = [
    path('', songs_player, name='player'),
]