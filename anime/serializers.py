from rest_framework import serializers

from .models import Useranime

class useranime(serializers.ModelSerializer):

    class Meta:
        model  = Useranime
        fields = ['user' , 'favgenres ']