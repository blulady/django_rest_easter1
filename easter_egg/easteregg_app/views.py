from django.shortcuts import render
from rest_framework import viewsets
from .models import Easter_egg_name
from .serializers import Easter_egg_nameSerializer


class Easter_egg_nameView(viewsets.ModelViewSet):
    queryset = Easter_egg_name.objects.all()
    serializer_class = Easter_egg_nameSerializer

