# Generated by Django 3.1.4 on 2021-01-01 21:59

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1009_auto_20201216_2005"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savedviewfilterrule",
            name="value",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
