# Generated by Django 4.2.4 on 2023-08-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_alter_vacancy_description_alter_vacancy_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary_per_hour_fixed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ставка почасовая (если нет месячной) (zlot)'),
        ),
    ]
