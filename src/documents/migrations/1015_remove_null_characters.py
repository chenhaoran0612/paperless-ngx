# Generated by Django 3.1.7 on 2021-04-04 18:28
import logging

from django.db import migrations

logger = logging.getLogger("paperless.migrations")


def remove_null_characters(apps, schema_editor):
    Document = apps.get_model("documents", "Document")

    for doc in Document.objects.all():
        content: str = doc.content
        if "\0" in content:
            logger.info(f"Removing null characters from document {doc}...")
            doc.content = content.replace("\0", " ")
            doc.save()


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1014_auto_20210228_1614"),
    ]

    operations = [
        migrations.RunPython(remove_null_characters, migrations.RunPython.noop),
    ]
