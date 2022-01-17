from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.prefetch_related( 'lessons', 'lessons__exercises')
    serializer_class = ModuleSerializer
