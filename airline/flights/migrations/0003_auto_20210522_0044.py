# Generated by Django 3.2.2 on 2021-05-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210521_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airpot',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='airpot',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
