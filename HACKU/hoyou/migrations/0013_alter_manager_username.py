# Generated by Django 4.2.5 on 2023-09-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hoyou", "0012_alter_manager_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
