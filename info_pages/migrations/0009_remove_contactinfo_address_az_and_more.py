# Generated by Django 4.2.4 on 2024-04-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_pages', '0008_remove_socialnetwork_name_az_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_az',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_pl',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_ru',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_uk',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_url_az',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_url_en',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_url_pl',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_url_ru',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='address_url_uk',
        ),
    ]
