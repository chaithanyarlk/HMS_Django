# Generated by Django 3.0.6 on 2020-11-08 07:43

from django.db import migrations, models
import institute.models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0004_auto_20201104_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=institute.models.Student.photo_storage_path),
        ),
    ]
