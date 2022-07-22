from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('easteregg_app', views.Easter_egg_nameView)

urlpatterns = [
    path('', include(router.urls))
]