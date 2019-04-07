from django.urls import path
from . import views
from rest_framework import routers
from .views import WorkViewSet, SkillViewSet, LinkViewSet

router = routers.DefaultRouter()
router.register(r'works', WorkViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'links', LinkViewSet)
