# Generated by Django 3.1.8 on 2021-11-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resturant',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
