# Generated by Django 4.0.6 on 2022-11-17 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TSApp', '0003_tsteacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('s_date', models.DateField()),
                ('e_date', models.DateField()),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ctask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('s_date', models.DateField()),
                ('e_date', models.DateField()),
                ('pgrs', models.IntegerField(blank=True, default='', null=True)),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]