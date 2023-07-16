# Generated by Django 4.1.6 on 2023-06-12 5:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0002_rename_traits_trait"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]