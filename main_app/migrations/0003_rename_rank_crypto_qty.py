# Generated by Django 4.0.6 on 2022-07-16 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_crypto_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='rank',
            new_name='qty',
        ),
    ]
