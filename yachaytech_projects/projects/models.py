from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=4)
    img = models.CharField(default ="",max_length=40)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="projects_school")
    comments = models.ManyToManyField(User, blank=True, related_name="reviews", through='Review')
    user = models.ForeignKey(User, default = "", on_delete=models.CASCADE, related_name="projects_user")

    def __str__(self):
        return f"{self.name} - {self.state} ({self.school})"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.username} - {self.project.name}: {self.comment}"