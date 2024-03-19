from rest_framework import serializers
from .models import Person


class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")
        return data