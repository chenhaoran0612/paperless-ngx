# Generated by Django 1.9 on 2016-01-29 22:58

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0007_auto_20160126_2114"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="file_type",
            field=models.CharField(
                choices=[
                    ("pdf", "PDF"),
                    ("png", "PNG"),
                    ("jpg", "JPG"),
                    ("gif", "GIF"),
                    ("tiff", "TIFF"),
                ],
                default="pdf",
                editable=False,
                max_length=4,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="document",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="documents",
                to="documents.Tag",
            ),
        ),
    ]
