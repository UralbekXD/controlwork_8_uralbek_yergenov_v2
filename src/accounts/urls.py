from django.urls import path

from .views import SignUpView, LoginView, logout_view
from .views import ProfileDetailView, ProfileEditView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

    # Profile
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name='profile_edit'),
]
