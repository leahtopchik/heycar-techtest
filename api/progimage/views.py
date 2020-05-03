from django.contrib.auth.models import User, Group
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    GenericViewSet
):
    """
    API endpoint that allows images to be uploaded.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
