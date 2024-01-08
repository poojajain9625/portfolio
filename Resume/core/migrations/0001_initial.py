# Generated by Django 5.0 on 2024-01-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=70)),
                (
                    "email",
                    models.CharField(
                        error_messages={"unique": "E-Mail id must be unique."},
                        max_length=100,
                        unique=True,
                    ),
                ),
                ("subject", models.TextField(max_length=100)),
                ("meassage", models.TextField(max_length=1000)),
            ],
        ),
    ]
