from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bachha", null=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher", null=True, default=None)


class Leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    comment = models.TextField(blank=True, null=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(null=True)

    def get_absolute_url(self):
        return reverse('index', kwargs=None)
