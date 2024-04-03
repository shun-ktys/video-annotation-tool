from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('/', views.index),
    path('videos/', views.VideoList.as_view()),
    path('videos/<int:pk>/', views.VideoDetail.as_view()), 
    path('videos/upload/', views.VideoUploadView.as_view()),
    path('users/', views.UserCreate.as_view()),
]