from django.contrib import admin
from django.urls import path, include

from .views import ThemeListView, ThemeDetailView, ThemeAddView, ThemeEditView, ThemeDeleteView
from .views import ReplyAddView

urlpatterns = [
    # Theme
    path('', ThemeListView.as_view(), name='themes'),
    path('theme/<int:pk>/detail/', ThemeDetailView.as_view(), name='theme_detail'),
    path('theme/add/', ThemeAddView.as_view(), name='theme_create'),
    path('theme/<int:pk>/edit/', ThemeEditView.as_view(), name='theme_update'),
    path('theme/<int:pk>/delete/', ThemeDeleteView.as_view(), name='theme_delete'),

    # Replies
    path('theme/<int:pk>/reply/create/', ReplyAddView.as_view(), name='reply_create')
]