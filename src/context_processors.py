from django.conf import settings
from django.core.urlresolvers import reverse

def main(request):
    is_active = {
        'index': request.path == reverse('main-index'),
    }
    return {
        'IS_ACTIVE': is_active,
        'SITE_DOMAIN': settings.SITE_DOMAIN,
        'SITE_NAME': settings.SITE_NAME,
    }