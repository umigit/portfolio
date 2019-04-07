from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .models import Work, Skill, Link
from .serializer import WorkSerializer, SkillSerializer, LinkSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
