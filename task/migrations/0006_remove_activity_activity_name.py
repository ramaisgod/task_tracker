# Generated by Django 2.1.5 on 2019-09-05 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_name',
        ),
    ]
