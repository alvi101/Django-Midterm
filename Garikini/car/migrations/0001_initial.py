# Generated by Django 5.0 on 2024-02-02 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("brand", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("thumbnail", models.ImageField(upload_to="uploads/")),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="brand.brand"
                    ),
                ),
            ],
        ),
    ]
