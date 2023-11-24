from django.shortcuts import render

from service.clients.serializers import UserSerializer
from service.tasks import welcome_email
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        welcome_email.delay(user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
