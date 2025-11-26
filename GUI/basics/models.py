from django.db import models

# Create your models here.

class StudentDepartment(models.Model):
    DEPT_NAME = models.CharField(max_length=500)
    DEPT_DESC = models.CharField(max_length=500)

    def __str__(self):
        return self.DEPT_NAME
