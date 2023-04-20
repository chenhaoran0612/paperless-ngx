# Generated by Django 1.9.4 on 2016-03-25 21:11

import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0012_auto_20160305_0040"),
    ]

    operations = [
        migrations.AddField(
            model_name="correspondent",
            name="match",
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name="correspondent",
            name="matching_algorithm",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Any"),
                    (2, "All"),
                    (3, "Literal"),
                    (4, "Regular Expression"),
                ],
                default=1,
                help_text='Which algorithm you want to use when matching text to the OCR\'d PDF.  Here, "any" looks for any occurrence of any word provided in the PDF, while "all" requires that every word provided appear in the PDF, albeit not in the order provided.  A "literal" match means that the text you enter must appear in the PDF exactly as you\'ve entered it, and "regular expression" uses a regex to match the PDF.  If you don\'t know what a regex is, you probably don\'t want this option.',
            ),
        ),
        migrations.AlterField(
            model_name="document",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name="log",
            name="component",
        ),
    ]
