# Generated by Django 5.1.6 on 2025-02-20 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_anexo_id_leiloeiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='id_leiloeiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.leiloeiro'),
        ),
    ]
