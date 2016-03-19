from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, RichText
from mezzanine.utils.models import AdminThumbMixin, upload_to
from django.utils.translation import ugettext_lazy as _


class Content(Displayable, RichText, AdminThumbMixin):
    featured_image = FileField(verbose_name=_("Featured Image"),
                               upload_to=upload_to("owacontent.Content.featured_image", "content"),
                               format="Image", max_length=255, null=True, blank=True)
    content_type = models.CharField(max_length=100, null=False, default="article")
    featured_piece = models.BooleanField(default=False)
    featured_piece_slide_image = FileField(verbose_name=_("Featured Piece Image"),
                               upload_to=upload_to("owacontent.Content.featured_piece_slide_image", "content"),
                               format="Image", max_length=255, null=True, blank=True)
    admin_thumb_field = "featured_image"

    class Meta:
        verbose_name = _("Content")
        verbose_name_plural = _("Content")
        ordering = ("-publish_date",)

    def get_absolute_url(self):
        return reverse("content_detail", kwargs={"slug": self.slug})
