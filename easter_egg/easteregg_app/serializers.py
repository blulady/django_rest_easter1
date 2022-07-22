from rest_framework import serializers
from .models import Easter_egg_name


class Easter_egg_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Easter_egg_name
        fields = ('id', 'name')
