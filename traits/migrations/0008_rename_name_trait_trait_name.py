# Generated by Django 4.1.6 on 2023-06-12 5:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0007_rename_trait_name_trait_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trait",
            old_name="name",
            new_name="trait_name",
        ),
    ]
