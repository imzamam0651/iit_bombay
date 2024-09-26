from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseInstanceViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'instances', CourseInstanceViewSet, basename='instances')

urlpatterns = [
    path('', include(router.urls)),
]