"""
Stores main models of the project
"""
from django.db import models
from PIL import Image
from io import BytesIO


class PhotoItem(models.Model):
    """
    Abstract
    help to store information about the photo
    """
    id = models.AutoField(primary_key=True)
    photo = models.ImageField('Изображение', height_field='height', width_field='width', null=True, blank=True)
    alt = models.TextField("Описание фото", max_length=200, blank=True, null=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    binary_image = models.BinaryField(null=True)
    ext = models.CharField(max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo.open()
            with BytesIO() as output:
                with Image.open(self.photo) as img:
                    self.ext = img.format
                    img.save(output, self.ext)
                self.binary_image = output.getvalue()

            if self.alt == '':
                self.alt = self.photo.name
        else:
            self.binary_image = None
        super(PhotoItem, self).save(*args, **kwargs)

    class Meta:
        """
        PhotoItem model settings
        """
        abstract = True
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
