# Generated by Django 4.1 on 2023-09-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoyou', '0021_person_vector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='person_image/'),
        ),
    ]
