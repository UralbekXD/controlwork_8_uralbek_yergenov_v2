from django.urls import path

from .views import SignUpView, LoginView, logout_view
# from .views import ProfileDetailView, ProfileEditView
# from .views import FollowUserView
# from .views import UnfollowUserView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

    # Profile
    # path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    # path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name='profile_edit'),
    #
    # path('profile/<int:pk>/follow/', FollowUserView.as_view(), name='follow'),
    # path('profile/<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow'),
]
