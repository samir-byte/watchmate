from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value)< 2:
        raise serializers.ValidationError("name must be greater than 2 characters")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.active = validated_data.get('active')
        instance.save()
        return instance

    # def validate_name(self, value):
    #     if len(value)< 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and descriptions should be differents")
        return data
