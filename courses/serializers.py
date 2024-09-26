from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']


class CourseInstanceSerializer(serializers.ModelSerializer):
    # course = CourseSerializer(read_only=True)
    # course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_id', 'year', 'semester']