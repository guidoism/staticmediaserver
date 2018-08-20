from django.db import models
from django.utils.safestring import mark_safe

class Movie(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=512)
    path = models.CharField(max_length=512)
    pic = models.ImageField()

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="/images/%s" width="100px"/>' % self.pic)

    image_tag.short_description = 'Image'

