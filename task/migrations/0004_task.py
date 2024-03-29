# Generated by Django 2.1.5 on 2019-09-05 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190905_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_owner', models.CharField(blank=True, max_length=255, null=True)),
                ('task_start', models.DateField(blank=True, null=True)),
                ('task_end', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('IN-PROCESS', 'IN-PROCESS'), ('ON-HOLD', 'ON-HOLD'), ('CANCELLED', 'CANCELLED')], default='IN-PROCESS', max_length=255)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Project')),
            ],
        ),
    ]
