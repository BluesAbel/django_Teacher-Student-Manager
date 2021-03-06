# Generated by Django 3.0.4 on 2020-03-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_show', '0002_delete_work_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Student',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField(max_length=128)),
                ('stu_id', models.IntegerField(max_length=128)),
                ('end_src', models.CharField(max_length=128)),
                ('studentname', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=128)),
                ('stu_desc', models.CharField(max_length=128)),
                ('work_src', models.CharField(max_length=128)),
                ('work_score', models.IntegerField(max_length=128)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'work2',
                'verbose_name_plural': 'work2',
                'ordering': ['c_time'],
            },
        ),
    ]
