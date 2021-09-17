from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset,many=True)
        return Response(serializer.data)