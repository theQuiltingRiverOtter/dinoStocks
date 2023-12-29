# Generated by Django 5.0 on 2023-12-28 20:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicals_app', '0001_initial'),
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicals',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicals',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicals',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicals', to='portfolio_app.portfolio', unique=True),
        ),
    ]