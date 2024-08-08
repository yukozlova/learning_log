# Generated by Django 5.0.7 on 2024-08-06 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learning_log", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("text", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_log.topic",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "entries",
            },
        ),
    ]
