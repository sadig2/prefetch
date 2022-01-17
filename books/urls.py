

from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register("", ModuleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
