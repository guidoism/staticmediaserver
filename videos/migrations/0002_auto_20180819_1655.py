# Generated by Django 2.1 on 2018-08-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Movie',
        ),
    ]