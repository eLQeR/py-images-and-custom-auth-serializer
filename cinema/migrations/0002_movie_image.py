# Generated by Django 4.1 on 2024-02-29 14:53

import cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=None, upload_to=cinema.models.create_custom_path),
            preserve_default=False,
        ),
    ]
