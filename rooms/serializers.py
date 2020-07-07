from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer(read_only=True)
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ("modified",)
        read_only_fields = [
            "user",
            "id",
            "created",
            "updated",
        ]

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    """
    {"name": "Good Room", "address": "Seoul", "price": 10, "beds": 1, "lat": 12, "lng": 12, "bedrooms": 1, "bathrooms": 1, "check_in": "14:00", "check_out": "12:00", "instant_book": false}
    """

    def validate(self, data):
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializer.ValidationError("Not enough time between change")
        return data

    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

    def create(self, validated_data):
        request = self.context.get("request")
        room = Room.objects.create(**validated_data, user=request.user)
        return room

