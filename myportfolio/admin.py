from django.contrib import admin
from .models import Work, Skill, Link

@admin.register(Work)
class Work(admin.ModelAdmin):
    pass

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    pass

@admin.register(Link)
class Link(admin.ModelAdmin):
    pass
