# Generated by Django 3.2 on 2023-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
