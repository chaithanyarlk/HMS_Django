# Generated by Django 3.0.6 on 2020-11-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_auto_20201106_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='type',
            field=models.CharField(max_length=40),
        ),
    ]
