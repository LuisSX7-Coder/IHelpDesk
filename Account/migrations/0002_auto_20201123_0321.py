# Generated by Django 3.0.5 on 2020-11-23 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_superuser',
            new_name='is_staff',
        ),
    ]
