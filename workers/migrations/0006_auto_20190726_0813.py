# Generated by Django 2.2.3 on 2019-07-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_auto_20190725_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='binary_image',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='binary_image',
            field=models.BinaryField(null=True),
        ),
    ]
