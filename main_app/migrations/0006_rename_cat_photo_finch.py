# Generated by Django 4.2.9 on 2024-01-12 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='finch',
        ),
    ]