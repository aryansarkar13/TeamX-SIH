from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import *
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser
from users.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone
import datetime


class RegistrationView(APIView):

    @swagger_auto_schema(
        operation_id='create_user',
        request_body=RegistrationSerializer,
        responses={

        },
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({}, status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    @swagger_auto_schema(
        operation_id='login_user',
        request_body=LoginSerializer,
        responses={

        },
    )
    def post(self, request):
        return Response({'token': f"Token none"}, status.HTTP_202_ACCEPTED)
        # serializer = LoginSerializer(data=request.data)

        # if serializer.is_valid():
        #     found_phone = serializer.data['phone']

        #     user = authenticate(
        #         username=serializer.data['phone'],
        #         password=serializer.data['password']
        #     )
        #     if user:
        #         token, _ = Token.objects.get_or_create(user=user)
        #         return Response({'token': f"Token {token.key}"}, status.HTTP_202_ACCEPTED)
        #     else:
        #         try:
        #             if User.objects.get(phone=found_phone):
        #                 return Response({'detail': 'Credentials did not match'}, status.HTTP_401_UNAUTHORIZED)

        #         except User.DoesNotExist:
        #             return Response({"detail": "User not found"}, status.HTTP_404_NOT_FOUND)
        # else:
        #     data = serializer.errors
        #     return Response(data, status.HTTP_400_BAD_REQUEST)


class RealtimeView(APIView):
    @swagger_auto_schema(
        operation_id='realtime_update',
        request_body=RealtimeSerializer,
        responses={

        },
    )
    def put(self, request):
        user = request.user
        serializer = RealtimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
