from django.db import models
from .choice import *

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_owner = models.CharField(max_length=255, null=True, blank=True)
    project_location = models.CharField(max_length=255, null=True, blank=True)
    project_type = models.CharField(max_length=255, null=True, blank=True)
    project_start = models.DateField(null=True, blank=True)
    project_end = models.DateField(null=True, blank=True)
    project_user = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(max_length=255, default='LOW', choices=CHOICE_PRIORITY)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, default='IN-PROCESS', choices=CHOICE_PROJECT_STATUS)

    def __str__(self):
        return self.project_name

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_owner = models.CharField(max_length=255, null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_start = models.DateField(null=True, blank=True)
    task_end = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, default='IN-PROCESS', choices=CHOICE_TASK_STATUS)

    def __str__(self):
        return self.task_name

class Activity(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    # activity_name = models.CharField(max_length=255)
    activity_owner = models.CharField(max_length=255, null=True, blank=True)
    activity_start = models.DateField(null=True, blank=True)
    activity_end = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, default='IN-PROCESS', choices=CHOICE_TASK_STATUS)

    def __str__(self):
        return self.description


