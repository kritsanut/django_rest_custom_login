from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#
#         return Response({'token': token.key, 'id': token.user_id})

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'id': user.pk,
            # 'password': user.password,
            'last_login': user.last_login,
            'is_superuser': user.is_superuser,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined
        })
