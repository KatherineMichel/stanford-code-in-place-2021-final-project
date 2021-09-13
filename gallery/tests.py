from django.test import TestCase
from model_bakery import baker

from .models import Artwork, Image


class ModelTestCase(TestCase):
    """A class that tests each model"""

    def test_artwork_model(self):
        artwork = baker.make(Artwork)
        assert artwork.title
