# Generated by Django 2.2.1 on 2019-11-03 14:52

import checker.virdicts
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import enumfields.fields
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team_size', models.IntegerField(default=4)),
                ('startDate', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 3, 14, 52, 30, 264495, tzinfo=utc))),
                ('finishDate', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 3, 14, 52, 30, 264517, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contests',
                'verbose_name': 'Contest',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('right_answer', models.CharField(max_length=200)),
                ('title', models.CharField(default='Task', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('checker', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checker.Checker')),
                ('solvers', models.ManyToManyField(related_name='solver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'verbose_name': 'Task',
            },
        ),
        migrations.CreateModel(
            name='TaskCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardness', enumfields.fields.EnumField(default='MIDDLE', enum=tasks.models.Hardness, max_length=500)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
            options={
                'verbose_name_plural': 'TasksCase',
                'verbose_name': 'TaskCase',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('general_name', models.CharField(default='Геометрия', max_length=200)),
                ('hardness', enumfields.fields.EnumField(default='MIDDLE', enum=tasks.models.Hardness, max_length=500)),
                ('tasks', models.ManyToManyField(through='tasks.TaskCase', to='tasks.Task')),
            ],
            options={
                'verbose_name_plural': 'Themes',
                'verbose_name': 'Theme',
            },
        ),
        migrations.CreateModel(
            name='TaskContestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Contest')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
            options={
                'verbose_name_plural': 'TaskContestCases',
                'verbose_name': 'TaskContestCase',
            },
        ),
        migrations.AddField(
            model_name='taskcase',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Theme'),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=20000)),
                ('verdict', enumfields.fields.EnumField(default='WRONG_ANSWER', enum=checker.virdicts.Virdict, max_length=500)),
                ('submitTime', models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 3, 14, 52, 30, 263901, tzinfo=utc))),
                ('judgerComment', models.CharField(max_length=20000)),
                ('task', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Solutions',
                'verbose_name': 'Solution',
            },
        ),
        migrations.AddField(
            model_name='contest',
            name='tasks',
            field=models.ManyToManyField(through='tasks.TaskContestCase', to='tasks.Task'),
        ),
    ]
