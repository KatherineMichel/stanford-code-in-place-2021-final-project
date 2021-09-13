from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


def upload_gallery_image(self, filename):
    return f"artworks/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    artwork = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, related_name="images"
    )
