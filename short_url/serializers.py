from rest_framework import serializers
from .models import ShortUrlModel


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrlModel
        fields = ('id', 'url', 'code')

