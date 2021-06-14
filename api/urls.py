from django.urls import path, include
from rest_framework import routers
from .views import HeroViewSet

routers = routers.DefaultRouter()
routers.register(r'heroes', HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally we include Login URLs for the browsable API

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
