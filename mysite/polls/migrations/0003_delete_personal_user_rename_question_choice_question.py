# Generated by Django 4.2.6 on 2023-10-17 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_personal_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal_user',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
    ]
