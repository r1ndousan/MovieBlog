# Generated by Django 4.2.19 on 2025-03-31 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 12, 43, 27, 695286), verbose_name='Опубликована'),
        ),
    ]
