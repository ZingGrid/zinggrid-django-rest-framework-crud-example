# serializers.py
from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        # id is auto generated primary key
        fields = ('id','name', 'alias', 'age', 'email')