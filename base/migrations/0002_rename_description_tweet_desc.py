# Generated by Django 4.1.3 on 2022-12-02 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='description',
            new_name='desc',
        ),
    ]