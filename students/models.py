from django.db import models
import uuid


class Student(models.Model):
    student_id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=37, editable=False)
    name = models.CharField(max_length=240)
    email = models.EmailField()
    document = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name
