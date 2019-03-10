# Generated by Django 2.1 on 2019-03-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190306_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='person',
            name='info',
            field=models.TextField(blank=True, verbose_name='Основная информация'),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FilePathField(null=True, path='C:\\Users\\gonch\\PycharmProjects\\psycho\\main\\static\\images', verbose_name='Фотография'),
        ),
    ]
