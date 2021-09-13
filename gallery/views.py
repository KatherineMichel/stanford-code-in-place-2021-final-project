from django.shortcuts import render
from .models import Artwork


def gallery_view(request):
    artwork = Artwork.objects.all()  # [:9]
    return render(request, "index.html", {"artwork": artwork})


def artwork_view(request, pk):
    artwork = Artwork.objects.get(id=pk)
    return render(request, "artwork.html", {"artwork": artwork})
