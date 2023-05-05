from rest_framework import serializers
from .models import Car
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'
