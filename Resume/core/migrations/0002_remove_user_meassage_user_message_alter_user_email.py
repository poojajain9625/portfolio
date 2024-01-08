# Generated by Django 4.2.6 on 2024-01-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="meassage",
        ),
        migrations.AddField(
            model_name="user",
            name="message",
            field=models.CharField(default="default_message_value", max_length=300),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=100),
        ),
    ]
