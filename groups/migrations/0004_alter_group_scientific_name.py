# Generated by Django 4.1.6 on 2023-06-12 5:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0003_alter_group_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="scientific_name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
