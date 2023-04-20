# Generated by Django 1.9 on 2016-01-14 18:44

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0003_sender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="sender",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="documents",
                to="documents.Sender",
            ),
        ),
    ]
