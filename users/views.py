from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import ReadUserSerilaizer


class MeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(ReadUserSerilaizer(request.user).data)

    def put(self, reuqest):
        pass


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerilaizer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

