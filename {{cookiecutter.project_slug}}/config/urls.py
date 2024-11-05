from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from {{ cookiecutter.project_slug }} import views

admin.site.site_header = admin.site.site_title = settings.ADMIN_SITE_HEADER


urlpatterns = [
    path("", views.index, name="index"),
    path("account/", include("allauth.urls")),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("covers/<int:size>/cover.webp", views.cover_image, name="cover_image"),
    path("robots.txt", views.robots, name="robots"),
    path("service-worker.js", views.service_worker, name="service_worker"),
    path("manifest.json", views.manifest, name="manifest"),
    path("favicon.ico", views.favicon, name="favicon"),
    path(".well-known/assetlinks.json", views.assetlinks, name="assetlinks"),
    path(".well-known/security.txt", views.security, name="security"),
    path("ht/", include("health_check.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]


if "django_browser_reload" in settings.INSTALLED_APPS:  # pragma: no cover
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if "debug_toolbar" in settings.INSTALLED_APPS:  # pragma: no cover
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]