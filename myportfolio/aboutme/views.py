from django.shortcuts import render

# django_spectacular
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SkillAndExperience
from .serializers import SkillAndExperienceSerializer


class SkillAndExperienceViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing all Skills and Experiences
    """
    queryset = SkillAndExperience.objects.all()

    @extend_schema(responses=SkillAndExperienceSerializer)
    def list(self, request):
        serializer = SkillAndExperienceSerializer(self.queryset, many=True)
        return Response(serializer.data)
