from django.urls import path
from .views import RegisterView,LoginView,CampaignList,LogoutView,CampaignView,DonationView,DonationList
# from rest_framework.routers import DefaultRouter
# from .views import CampaignViewSet, DonationViewSet

# router = DefaultRouter()
# router.register(r'campaigns', CampaignViewSet)
# router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('campaignlist/',CampaignList.as_view(),name='campaignlist'),
    path('campaign/',CampaignView.as_view(),name='campaign'),
    path('campaign/<int:pk>/',CampaignView.as_view(),name='campaign_edit_delete'),
    path('donation/',DonationView.as_view(),name='donation'),
    path('donationlist/',DonationList.as_view(),name='donationlist'),
    path('donation/<int:pk>/',DonationView.as_view(),name='donation_edit_delete')



]
