# Generated by Django 3.0.2 on 2020-06-04 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sites',
            name='lastTime',
        ),
    ]
