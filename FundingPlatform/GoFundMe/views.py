from rest_framework import viewsets
from .models import Campaign, Donation
from .serializers import CampaignSerializer, DonationSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
# class CampaignViewSet(viewsets.ModelViewSet):
#     queryset = Campaign.objects.all()
#     serializer_class = CampaignSerializer

# class DonationViewSet(viewsets.ModelViewSet):
#     queryset = Donation.objects.all()
#     serializer_class = DonationSerializer

class RegisterView(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Signup Sucessfull','data': serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    def post(self,request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request,username=username,password=password)

        if not user: raise AuthenticationFailed('Unauthorized')

        payload = {'id' : user.id, 'exp' : datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=5)}
        token = jwt.encode(payload,'cap004',algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwtToken',value=token)
        response.data = {'message': 'Login Sucessfull','token' : token}
        return response


    
        
        
    