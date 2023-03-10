# from django.conf.urls import include, url
# -from django.conf.urls import include, url
from django.conf.urls import include
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

from .views import ResourcesViewset

router = DefaultRouter()
router.register('resources', ResourcesViewset, basename='resources')

urlpatterns = [
    url('^api/', include((router.urls, 'api'), namespace='api')),
]
