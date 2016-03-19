from __future__ import unicode_literals

from django.db import models

# Create your models here.
from mezzanine.core.models import Displayable, RichText
from mezzanine.utils.models import AdminThumbMixin


class Content(Displayable, RichText, AdminThumbMixin):
    
    pass