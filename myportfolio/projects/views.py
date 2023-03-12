from django.shortcuts import render

# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, Tag
from .serializers import ProjectSerializer, TagSerializer


class ProjectsViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all products
    """

    queryset = Project.objects.all()

    @extend_schema(responses=ProjectSerializer)
    def list(self, request):
        serializer = ProjectSerializer(self.queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all tags
    """

    queryset = Tag.objects.all()

    @extend_schema(responses=TagSerializer)
    def list(self, request):
        serializer = TagSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class ListProjects(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    """
    ListProjects
    """
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        query = Project.objects.all()
        serializer = ProjectSerializer(query, many=True)

        return Response(serializer.data)