# from django.shortcuts import render
import requests

from rest_framework import generics, permissions, serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from django.contrib.auth.models import User

# from django.contrib.auth.models import User, Group
# from rest_framework.views import APIView


# from auth.serializers import UserSerializer

# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class Test(APIView):
#     def get(self, request, format=None):
#         print('Hi', request)


class AuthViewSet(APIView):
    queryset = User.objects.all()

    def get(self, request):
        state = request.GET.get('state')
        code = request.GET.get('code')

        payload = {
            'state': state,
            'code': code,
        }

        print('payload', payload)

        headers = {'content-type': 'application/x-www-form-urlencoded'}

        try:
            response = requests.post(
                'http://localhost:8000/auth/o/vk-oauth2/', params=payload, headers=headers)
            print(response.text)
            return Response(response.text)
        except Exception as e:
            print('ok', e)

        return Response('hello')
