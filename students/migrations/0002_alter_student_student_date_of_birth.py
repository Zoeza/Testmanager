# Generated by Django 4.0.4 on 2022-05-27 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 5, 27, 16, 40, 2, 191334)),
        ),
    ]
