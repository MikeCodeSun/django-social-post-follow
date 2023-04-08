from django.urls import path
from .views import dashboard, profile_list, profile

app_name = 'twitter'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name="profile_list"),
    path('profile/<int:id>/', profile, name='profile'),
]
