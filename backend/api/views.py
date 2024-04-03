from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from rest_framework import generics
from .serializers import VideoSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

class VideoUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES['file']
        video = Video(file=file)
        video.save()
        return Response(status=status.HTTP_201_CREATED)
    
class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer