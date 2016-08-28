from django.test import TestCase
from django.utils import timezone

from .models import Course


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title = "Python Regular Exp",
            description = "Learn to write regex"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)