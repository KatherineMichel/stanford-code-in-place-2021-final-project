from django.shortcuts import render
from .models import Artwork

def gallery_view(request):
    artwork = Artwork.objects.all()# [:9]
    return render(request, 'index.html', {"artwork":artwork})

