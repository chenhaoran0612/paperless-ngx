# Generated by Django 1.9 on 2015-12-20 19:10

from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender", models.CharField(blank=True, db_index=True, max_length=128)),
                ("title", models.CharField(blank=True, db_index=True, max_length=128)),
                (
                    "content",
                    models.TextField(
                        db_index=(
                            "mysql" not in settings.DATABASES["default"]["ENGINE"]
                        ),
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
