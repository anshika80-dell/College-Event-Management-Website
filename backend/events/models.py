from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Registration(models.Model):
    student_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    event_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email", "event_name"],
                name="unique_email_per_event",
            )
        ]

    def __str__(self):
        return f"{self.student_name} - {self.event_name}"