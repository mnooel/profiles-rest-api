from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from . import views as profiles_views

router = DefaultRouter()
router.register('hello-viewset', profiles_views.HelloViewSet, basename='hello-viewset')
router.register('profile', profiles_views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', profiles_views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
