from rest_framework import serializers

from .models import SkillAndExperience

class SkillAndExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillAndExperience
        fields = "__all__"

