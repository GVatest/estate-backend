# Generated by Django 4.0.6 on 2022-07-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='massage',
            new_name='message',
        ),
    ]
