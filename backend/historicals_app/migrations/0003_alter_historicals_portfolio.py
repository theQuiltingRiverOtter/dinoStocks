# Generated by Django 5.0 on 2023-12-28 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicals_app', '0002_historicals_time_stamp_historicals_value_and_more'),
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicals',
            name='portfolio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='historicals', to='portfolio_app.portfolio'),
        ),
    ]
