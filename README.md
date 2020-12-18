Install python
Install Django
Install Django-Oscar
Install sorl-thumbnail
Install Pillow
Isntall django-oscar-paypal


Para ver y guardar imagenes que se agregan el sistema:

En Settings al final agregar:

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Luego agregar a la url para que se pueda mostrar las imagenes en el sistema

from django.conf import settings
from django.conf.urls.static import static

al final luego del ']' agregar lo siguiente: + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

A la hora de editar estilos que se importan se debe cambiar la referencia de Styles a otro nombre porque ya existe uno en uso