from rest_framework import serializers
from . import models

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = models.WatchList
        fields = '__all__'

    # def get_len_name(self, obj):
    #     return len(obj.name)
    # def validate(self, data):
    #     if len(data['name']) < 2:
    #         raise serializers.ValidationError("Name must be at least 2 characters long.")
        
    #     if data['name'] == data['des']:
    #         raise serializers.ValidationError("Name and description must be different.")
        
    #     return data



class PlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True) //it will show all fields of the watchlist
    watchlist = serializers.StringRelatedField(many=True, read_only=True) #it will show only the title fields of the watchlist
    class Meta:
        model = models.Platform
        fields = '__all__'



# def name_validator(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name must be at least 2 characters long.")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     des = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return models.Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.des = validated_data.get('des', instance.des)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # object level validation methods
#     def validate(self, data):
#         if len(data['name']) < 2:
#             raise serializers.ValidationError("Name must be at least 2 characters long.")
        
#         if data['name'] == data['des']:
#             raise serializers.ValidationError("Name and description must be different.")
#         return data
    
    # filed lavel validation method
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name must be at least 2 characters long.")
    #     return value