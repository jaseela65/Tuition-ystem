# Generated by Django 4.0.6 on 2022-11-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TSApp', '0008_rename_task_ctask_taske_alter_ctask_sid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='taske',
        ),
    ]
