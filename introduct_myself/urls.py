from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import introduct_myself_view

urlpatterns = [
    path('introduct/', introduct_myself_view, name='introduct'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
