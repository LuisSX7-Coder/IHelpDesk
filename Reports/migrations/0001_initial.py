# Generated by Django 3.0.5 on 2020-11-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_m_report', models.IntegerField()),
                ('project', models.CharField(max_length=50)),
                ('numer_tasks', models.IntegerField()),
                ('number_tasks_done', models.IntegerField()),
                ('number_tasks_unsolve', models.IntegerField()),
                ('number_tasks_in_progress', models.IntegerField()),
                ('percentage_tasks_done', models.IntegerField()),
                ('percentage_tasks_unsolve', models.IntegerField()),
                ('percentage_tasks_in_progress', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PriorityReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rtp_priority', models.IntegerField()),
                ('priority', models.CharField(max_length=50)),
                ('number_tasks_done', models.IntegerField()),
                ('number_tasks_unsolve', models.IntegerField()),
                ('number_tasks_in_progress', models.IntegerField()),
                ('percentage_tasks_done', models.IntegerField()),
                ('percentage_tasks_unsolve', models.IntegerField()),
                ('percentage_tasks_in_progress', models.IntegerField()),
            ],
        ),
    ]
