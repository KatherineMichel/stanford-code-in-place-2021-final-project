from django.urls import path

from .views import artwork_view, gallery_view

urlpatterns = [
    path("", gallery_view, name="index"),
    path("artwork/<int:pk>/", artwork_view, name="artwork"),
]
