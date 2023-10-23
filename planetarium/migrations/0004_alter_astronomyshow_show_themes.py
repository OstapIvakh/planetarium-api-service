# Generated by Django 4.2.6 on 2023-10-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planetarium", "0003_alter_astronomyshow_options_astronomyshow_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="astronomyshow",
            name="show_themes",
            field=models.ManyToManyField(
                blank=True, related_name="show_themes", to="planetarium.showtheme"
            ),
        ),
    ]
