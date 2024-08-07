import jwt
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Middleware
class JwtAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.exclude_path = [reverse('logins'), reverse('registers')]

    def __call__(self, request):
        if request.path in self.exclude_path or request.path.startswith('/admin'):
            return self.get_response(request)

        token = request.COOKIES.get('jwtToken')

        if token is None:
            return JsonResponse({'message': 'Authentication token not provided'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, 'cap004', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            return Response({'message': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        profile = User.objects.filter(user=payload['id']).first()
        request.user = profile

        return self.get_response(request)
