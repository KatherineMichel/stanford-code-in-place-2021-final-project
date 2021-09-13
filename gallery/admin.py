from django.contrib import admin
from .models import Artwork, Image

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
