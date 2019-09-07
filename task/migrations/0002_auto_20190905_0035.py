# Generated by Django 2.1.5 on 2019-09-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='LOW', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('IN-PROCESS', 'IN-PROCESS'), ('ON-HOLD', 'ON-HOLD')], default='IN-PROCESS', max_length=255),
        ),
    ]