# Generated by Django 3.2.4 on 2022-12-15 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='employee_id',
            new_name='users',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='user_name',
        ),
    ]
