# Generated by Django 4.2.4 on 2023-08-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HourlyPaymentOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=100, verbose_name='Тип оплаты (для студентов, ночные, испытательный и тд.)')),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Почасовая ставка')),
            ],
            options={
                'verbose_name': 'Вариант почасовой оплаты',
                'verbose_name_plural': 'Варианты почасовой оплаты',
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Индекс')),
            ],
            options={
                'verbose_name': 'Индекс',
                'verbose_name_plural': 'Индексы',
            },
        ),
        migrations.CreateModel(
            name='InfoLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=512, verbose_name='Жилье')),
                ('benefits', models.CharField(max_length=512, verbose_name='Выгоды')),
            ],
            options={
                'verbose_name': 'Описание Стандарт',
                'verbose_name_plural': 'Описания Стандарт',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл (Если нет ссылки на YT)')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на YouTube (если есть)')),
                ('embeded', models.CharField(blank=True, max_length=500, null=True, verbose_name='Встройка в YouTube (не изменять)')),
            ],
            options={
                'verbose_name': 'Видеозапись',
                'verbose_name_plural': 'Видеозаписи',
            },
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=64, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
                ('region_name', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('isp', models.CharField(blank=True, max_length=256, null=True)),
                ('mobile', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(unique=True, verbose_name='Описание обязанности')),
            ],
            options={
                'verbose_name': 'Обязанность по работе',
                'verbose_name_plural': 'Обязанности по работе',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('salary_per_mounth_min', models.IntegerField(blank=True, null=True, verbose_name='Ставка месячная минимум (zlot)')),
                ('salary_per_mounth_max', models.IntegerField(blank=True, null=True, verbose_name='Ставка месячная максимум (zlot)')),
                ('salary_per_mounth_fixed', models.IntegerField(blank=True, null=True, verbose_name='Ставка месячная фиксированая (если нет минимума или максимума) (zlot)')),
                ('salary_is_netto', models.BooleanField(default=True, verbose_name='Зарплата netto?')),
                ('work_schedule', models.TextField(blank=True, null=True, verbose_name='График работы')),
                ('description', models.TextField(verbose_name='Описание')),
                ('active', models.BooleanField(default=True, verbose_name='Активно')),
                ('card_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_card_photo', to='vacancy.photo', verbose_name='Картинка карточки вакансии и обложки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.category', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.city', verbose_name='Место работы')),
                ('index', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancy.index', verbose_name='Индекс (служебное)')),
                ('info_label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancy.infolabel', verbose_name='Описание стандарт')),
                ('photos', models.ManyToManyField(to='vacancy.photo', verbose_name='Фотографии вакансии')),
                ('salary_per_hour', models.ManyToManyField(to='vacancy.hourlypaymentoption', verbose_name='Варианты почасовой оплаты')),
                ('sex', models.ManyToManyField(to='vacancy.sex', verbose_name='Пол')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.state', verbose_name='Регион')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.video', verbose_name='Видеозапись вакансии')),
                ('views', models.ManyToManyField(to='vacancy.view')),
                ('work_duties', models.ManyToManyField(to='vacancy.workduty', verbose_name='Обязанности по работе')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['name'],
            },
        ),
    ]
