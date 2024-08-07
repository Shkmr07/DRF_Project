from rest_framework import serializers
from .models import Campaign, Donation
from django.contrib.auth.models import User

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        exclude = ['owner']
        

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        exclude = ['donor']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['first_name','last_name','username','password','email']
        extra_kextra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):

        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None: instance.set_password(password)
        instance.save()
        return instance 