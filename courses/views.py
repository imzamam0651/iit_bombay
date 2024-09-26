from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course ViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Override the destroy method to handle deletion
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Course Instance ViewSet
class CourseInstanceViewSet(viewsets.ModelViewSet):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    # List instances for a specific year and semester
    @action(detail=False, methods=['get'], url_path='(?P<year>[0-9]{4})/(?P<semester>[0-9]+)')
    def list_by_year_semester(self, request, year=None, semester=None):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)

    # Retrieve a specific instance by course ID, year, and semester
    @action(detail=False, methods=['get'], url_path='(?P<year>[0-9]{4})/(?P<semester>[0-9]+)/(?P<course_id>[0-9]+)')
    def retrieve_by_course(self, request, year=None, semester=None, course_id=None):
        instance = CourseInstance.objects.filter(course_id=course_id, year=year, semester=semester).first()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Override the destroy method to handle deletion
    @action(detail=False, methods=['delete'], url_path='(?P<year>[0-9]{4})/(?P<semester>[0-9]+)/(?P<course_id>[0-9]+)')
    def delete_instance(self, request, year=None, semester=None, course_id=None):
        instance = CourseInstance.objects.filter(course_id=course_id, year=year, semester=semester).first()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)