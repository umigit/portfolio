from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=64)
    detail = models.TextField(default="")
    url = models.URLField(default="")
    github_front = models.URLField(default="")
    github_back = models.URLField(default="")

class Skill(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField()

class Link(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()
