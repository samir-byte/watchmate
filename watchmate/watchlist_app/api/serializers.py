from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model= Review
        exclude = ('watchlist',)
        # fields =  "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields =  "__all__"  #to get all fields at once


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True) #to return only title of watchlist
    class Meta:
        model = StreamPlatform
        fields = "__all__"




        # fields = ['id', 'name', 'description'] #individual fields
        # exclude = ['active'] #if we don't want specifif field
        #if need to provide validation need to be put here
    #     def validate_name(self, value):
    #         if len(value)< 2:
    #             raise serializers.ValidationError("Name is too short!")
    #         return value

    #     def validate(self, data):
    #         if data['name'] == data['description']:
    #             raise serializers.ValidationError("Title and descriptions should be differents")
    #         return data

        
    # def get_len_name(self, object):
    #     return len(object.name)

# def name_length(value):
#     if len(value)< 2:
#         raise serializers.ValidationError("name must be greater than 2 characters")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.active = validated_data.get('active')
#         instance.save()
#         return instance

#     # def validate_name(self, value):
#     #     if len(value)< 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and descriptions should be differents")
#         return data
