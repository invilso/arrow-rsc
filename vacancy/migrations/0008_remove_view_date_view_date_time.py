# Generated by Django 4.2.4 on 2023-09-01 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0007_alter_vacancy_salary_per_hour_fixed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='date',
        ),
        migrations.AddField(
            model_name='view',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
