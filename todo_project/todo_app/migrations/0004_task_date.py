# Generated by Django 4.0.6 on 2022-07-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-12-10'),
            preserve_default=False,
        ),
    ]
