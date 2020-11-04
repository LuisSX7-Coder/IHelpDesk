from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False,null=False)
    client = models.CharField(max_length=50, blank=False, null=False)
    priority = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    phase = models.CharField(max_length=15, blank=False, null=False)

class Task(models.Model):
    task_name = models.CharField(max_length=20, blank=False, null=False)
    project = models.CharField(max_length=50, blank=False, null=False)
    priority = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    who_creates = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_open = models.BooleanField()

class Client(models.Model):
    id_client = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=50)

class Cycle(models.Model):
    id_cycle = models.IntegerField(primary_key=True)
    cycle_name = models.CharField(max_length=15)

class Team(models.Model):
    id_team = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=15)

class Systems(models.Model):
    id_system = models.IntegerField(primary_key=True)
    system_name = models.CharField(max_length=20)

class Phases(models.Model):
    id_phase = models.IntegerField(primary_key=True)
    phase_name = models.CharField(max_length=15)