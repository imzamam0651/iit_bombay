from django.db import models

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_code}: {self.title}"


# Course Instance model
class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.course.course_code} - {self.year} Semester {self.semester}"
