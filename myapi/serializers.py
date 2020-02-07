# serializers.py
from rest_framework import serializers

from .models import Hero, Todo

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        # id is auto generated primary key
        fields = ('id','name', 'alias', 'age', 'email')

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # id is auto generated primary key
        fields = ('id', 'item')