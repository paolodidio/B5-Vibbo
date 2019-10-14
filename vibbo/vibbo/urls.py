# accounts/urls.py
from django.urls import path
from .views import CreateProfileView, DisplayDetailView
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('change/', CreateProfileView.as_view(), name='change'),
    path('detail/<pk>', DisplayDetailView.as_view(), name='profile-detail')
]