from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r'^admin/ws/content_editing/(?P<room_name>.*)/',
        consumers.PresenceConsumer.as_asgi(),
    )
]
