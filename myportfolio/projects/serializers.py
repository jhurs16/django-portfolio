from rest_framework import serializers

from .models import Project, Tag 

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Tag
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"