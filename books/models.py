from statistics import mode

from django.db import models


class OnlineCourse(models.Model):
    title = models.CharField(max_length=255, default='')
    

class Module(models.Model):
    """
    A specific module for a course
    """
    title = models.CharField(max_length=255, default='')
    course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, null=True, related_name="modules")


class Lesson(models.Model):
    """
    A specific lesson in a module
    """
    title = models.CharField(max_length=255, default='')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, related_name="lessons")


class Exercise(models.Model):
    """
    A specific exercise for a lesson
    """
    TYPES = (
        ('vid', 'Video'),
        ('mcq', 'Multiple Choice Quiz'),
        ('fib', 'Fill in Blank'),
        ('text', 'Text Lesson')
    )
    type = models.CharField(max_length=255, default='video', choices=TYPES)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, related_name="exercises")   
