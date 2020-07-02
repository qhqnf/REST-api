from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room


class ReadRoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)


class WriteRoomSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    """
    {"name": "Good Room", "address": "Seoul", "price": 10, "beds": 1, "lat": 12, "lng": 12, "bedrooms": 1, "bathrooms": 1, "check_in": "14:00", "check_out": "12:00", "instant_book": false}
    """

    def validate(self, data):
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        if check_in == check_out:
            raise serializer.ValidationError("Not enough time between change")
        else:
            return data
