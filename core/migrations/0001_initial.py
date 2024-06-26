# Generated by Django 5.0.1 on 2024-05-14 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created_date')),
                ('company_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', max_length=255, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', max_length=255, verbose_name='Job Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created_date')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='Description')),
                ('parameters', models.CharField(blank=True, default='', max_length=255, verbose_name='Parameters')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created_date')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='Description')),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image Setting',
                'verbose_name_plural': 'Image Settings',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated_date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created_date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=255, verbose_name='Name')),
                ('percentage', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skill',
                'ordering': ('order',),
            },
        ),
    ]
