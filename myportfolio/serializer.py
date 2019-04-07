from rest_framework import serializers
from .models import Work, Skill, Link

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'detail', 'url', 'github_front', 'github_back', 'image')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'level')

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('name', 'url')
