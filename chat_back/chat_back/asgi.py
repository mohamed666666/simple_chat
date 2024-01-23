"""
ASGI config for chat_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from app.routing import websocket_urlpatterns



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_back.settings')

django_asgi_app = get_asgi_application()

import app.routing


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    # Just HTTP for now. (We can add other protocols later.)
})
