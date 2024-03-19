# Generated by Django 5.0.3 on 2024-03-17 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_person_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
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
                ("color_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="person",
            name="color",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="home.color"
            ),
        ),
    ]
