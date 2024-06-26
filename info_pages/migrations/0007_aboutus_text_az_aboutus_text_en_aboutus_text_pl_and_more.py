# Generated by Django 4.2.4 on 2024-04-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_pages', '0006_alter_contactinfo_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='text_az',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_pl',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_az',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_pl',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_az',
            field=models.CharField(max_length=150, null=True, verbose_name='Запрос для поиска в Google Maps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Запрос для поиска в Google Maps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_pl',
            field=models.CharField(max_length=150, null=True, verbose_name='Запрос для поиска в Google Maps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Запрос для поиска в Google Maps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Запрос для поиска в Google Maps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_url_az',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL встройки GMaps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_url_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL встройки GMaps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_url_pl',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL встройки GMaps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_url_ru',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL встройки GMaps'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='address_url_uk',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL встройки GMaps'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='description_az',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='description_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='description_pl',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='description_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='description_uk',
            field=models.CharField(max_length=250, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='title_az',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='title_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='guarantees',
            name='title_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='name_az',
            field=models.CharField(max_length=50, null=True, verbose_name='Назание документа'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Назание документа'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Назание документа'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Назание документа'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Назание документа'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='text_az',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='text_pl',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='legaldocument',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='partners',
            name='name_az',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Название партнера (для удобства)'),
        ),
        migrations.AddField(
            model_name='partners',
            name='name_en',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Название партнера (для удобства)'),
        ),
        migrations.AddField(
            model_name='partners',
            name='name_pl',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Название партнера (для удобства)'),
        ),
        migrations.AddField(
            model_name='partners',
            name='name_ru',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Название партнера (для удобства)'),
        ),
        migrations.AddField(
            model_name='partners',
            name='name_uk',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Название партнера (для удобства)'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone_number_az',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone_number_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone_number_pl',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone_number_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone_number_uk',
            field=models.CharField(max_length=30, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='name_az',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('x-twitter', 'Twitter'), ('snapchat', 'Snapchat'), ('whatsapp', 'WhatsApp'), ('viber', 'Viber')], max_length=15, null=True, verbose_name='Название социальной сети'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='name_en',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('x-twitter', 'Twitter'), ('snapchat', 'Snapchat'), ('whatsapp', 'WhatsApp'), ('viber', 'Viber')], max_length=15, null=True, verbose_name='Название социальной сети'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='name_pl',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('x-twitter', 'Twitter'), ('snapchat', 'Snapchat'), ('whatsapp', 'WhatsApp'), ('viber', 'Viber')], max_length=15, null=True, verbose_name='Название социальной сети'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='name_ru',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('x-twitter', 'Twitter'), ('snapchat', 'Snapchat'), ('whatsapp', 'WhatsApp'), ('viber', 'Viber')], max_length=15, null=True, verbose_name='Название социальной сети'),
        ),
        migrations.AddField(
            model_name='socialnetwork',
            name='name_uk',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('tiktok', 'TikTok'), ('linkedin', 'LinkedIn'), ('telegram', 'Telegram'), ('discord', 'Discord'), ('x-twitter', 'Twitter'), ('snapchat', 'Snapchat'), ('whatsapp', 'WhatsApp'), ('viber', 'Viber')], max_length=15, null=True, verbose_name='Название социальной сети'),
        ),
        migrations.AddField(
            model_name='team',
            name='name_az',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='team',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='team',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='team',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='team',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_az',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Должность'),
        ),
    ]
