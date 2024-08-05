from django.urls import path
from .views import RegisterView,LoginView
# from rest_framework.routers import DefaultRouter
# from .views import CampaignViewSet, DonationViewSet

# router = DefaultRouter()
# router.register(r'campaigns', CampaignViewSet)
# router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login')
]
