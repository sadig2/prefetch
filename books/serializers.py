from dataclasses import field, fields
from imp import source_from_cache
from multiprocessing import context

from rest_framework import serializers

from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = '__all__'
    def get_exercises(self, obj):
        qs = obj.exercises.all().order_by('id')
        return ExerciseSerializer(qs, many=True, read_only=True).data


class ModuleSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Module
        fields = '__all__'
    def get_lessons(self, obj):
        return LessonSerializer(obj.lessons.all().order_by('id').prefetch_related("exercises"), many=True, read_only=True ,context = self.context).data
