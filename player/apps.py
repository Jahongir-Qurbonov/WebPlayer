from django.apps import AppConfig


class PlayerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'player'

    def ready(self) -> None:
        from . import signals
        return super().ready()