# Generated by Django 3.2.3 on 2021-05-26 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='watch',
            new_name='watchlist',
        ),
    ]