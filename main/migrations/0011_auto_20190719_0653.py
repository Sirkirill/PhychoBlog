# Generated by Django 2.2.3 on 2019-07-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190719_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='alt',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание фото'),
        ),
        migrations.AlterField(
            model_name='articlephotoreport',
            name='alt',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='alt',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание фото'),
        ),
        migrations.AlterField(
            model_name='person',
            name='alt',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание фото'),
        ),
    ]
