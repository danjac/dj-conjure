import functools
import json
from typing import Final

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.shortcuts import resolve_url
from django.template.context import RequestContext
from django.utils.html import format_html



_SECONDS_IN_MINUTE: Final = 60
_SECONDS_IN_HOUR: Final = 3600

register = template.Library()


@register.simple_tag
def htmx_config() -> str:
    """Returns HTMX config in meta tag."""
    return format_html(
        '<meta name="htmx-config" content="{}">',
        json.dumps(settings.HTMX_CONFIG, cls=DjangoJSONEncoder),
    )


@register.simple_tag
@functools.cache
def get_site() -> Site:
    """Returns the current Site instance. Use when `request.site` is unavailable, e.g. in emails run from cronjobs."""

    return Site.objects.get_current()


@register.simple_tag
def absolute_uri(url: Model | str | None = None, *url_args, **url_kwargs) -> str:
    """Returns the absolute URL to site domain."""

    site = get_site()
    path = resolve_url(url, *url_args, **url_kwargs) if url else ""
    scheme = "https" if settings.SECURE_SSL_REDIRECT else "http"

    return f"{scheme}://{site.domain}{path}"


@register.simple_tag(takes_context=True)
def get_accept_cookies(context: RequestContext) -> bool:
    """Returns True if user has accepted cookies."""
    return settings.GDPR_COOKIE_NAME in context.request.COOKIES


