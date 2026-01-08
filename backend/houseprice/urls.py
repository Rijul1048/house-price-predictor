from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictor.urls')),
]

# Serve static files during development
if settings.DEBUG:
    from pathlib import Path
    urlpatterns += static(settings.STATIC_URL, document_root=Path(settings.STATICFILES_DIRS[0]))
