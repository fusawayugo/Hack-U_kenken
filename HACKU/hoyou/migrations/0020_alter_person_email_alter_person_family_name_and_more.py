# Generated by Django 4.2.5 on 2023-09-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hoyou", "0019_alter_person_family_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person", name="email", field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="person",
            name="family_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="person",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
    ]
