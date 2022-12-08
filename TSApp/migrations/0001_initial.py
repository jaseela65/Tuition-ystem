# Generated by Django 4.0.6 on 2022-11-05 19:20

import TSApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_date', models.DateField()),
                ('T_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.IntegerField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TSclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.TextField()),
                ('syllabus', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TSsubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TSteacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(validators=[TSApp.models.validate_capitalized])),
                ('address', models.TextField()),
                ('gender', models.TextField()),
                ('age', models.IntegerField()),
                ('mobile', models.TextField()),
                ('email', models.TextField()),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tssubject')),
            ],
        ),
        migrations.CreateModel(
            name='TSstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.TextField()),
                ('subjects', models.TextField()),
                ('address', models.TextField()),
                ('gender', models.TextField()),
                ('age', models.IntegerField()),
                ('mobile', models.TextField()),
                ('email', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsclass')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[TSApp.models.validate_capitalized])),
            ],
        ),
        migrations.CreateModel(
            name='rjt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.lv')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.TextField()),
                ('mal', models.IntegerField()),
                ('hid', models.IntegerField()),
                ('es', models.IntegerField()),
                ('ms', models.IntegerField()),
                ('ps', models.IntegerField()),
                ('cmy', models.IntegerField()),
                ('bgy', models.IntegerField()),
                ('ss', models.IntegerField()),
                ('inft', models.IntegerField()),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsclass')),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_date', models.DateField()),
                ('T_date', models.DateField()),
                ('status', models.TextField()),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lv',
            name='sid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent'),
        ),
        migrations.AddField(
            model_name='lv',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('paid', models.TextField()),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='axept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.lv')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atndns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('atndns', models.TextField()),
                ('sid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TSApp.tsstudent')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]