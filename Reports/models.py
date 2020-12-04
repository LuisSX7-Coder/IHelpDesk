from django.db import models

# Create your models here.
class MonthlyReport(models.Model):
    id_m_report = models.IntegerField()
    project = models.CharField(max_length=50)
    numer_tasks = models.IntegerField()
    number_tasks_done = models.IntegerField()
    number_tasks_unsolve = models.IntegerField()
    number_tasks_in_progress = models.IntegerField()
    percentage_tasks_done = models.IntegerField()
    percentage_tasks_unsolve = models.IntegerField()
    percentage_tasks_in_progress = models.IntegerField()

class WeeklyReport(object):
    id_w_report = models.IntegerField()
    project = models.CharField(max_length=50)
    numer_tasks = models.IntegerField()
    number_tasks_done = models.IntegerField()
    number_tasks_unsolve = models.IntegerField()
    number_tasks_in_progress = models.IntegerField()
    percentage_tasks_done = models.IntegerField()
    percentage_tasks_unsolve = models.IntegerField()
    percentage_tasks_in_progress = models.IntegerField()

class DailyReport(object):
    id_d_report = models.IntegerField()
    project = models.CharField(max_length=50)
    numer_tasks = models.IntegerField()
    number_tasks_done = models.IntegerField()
    number_tasks_unsolve = models.IntegerField()
    number_tasks_in_progress = models.IntegerField()
    percentage_tasks_done = models.IntegerField()
    percentage_tasks_unsolve = models.IntegerField()
    percentage_tasks_in_progress = models.IntegerField()

    class PriorityReports(models.Model):
        id_rtp_priority = models.IntegerField()
        priority = models.CharField(max_length=50)
        number_tasks_done = models.IntegerField()
        number_tasks_unsolve = models.IntegerField()
        number_tasks_in_progress = models.IntegerField()
        percentage_tasks_done = models.IntegerField()
        percentage_tasks_unsolve = models.IntegerField()
        percentage_tasks_in_progress = models.IntegerField()
