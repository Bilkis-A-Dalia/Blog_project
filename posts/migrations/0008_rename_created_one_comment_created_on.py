# Generated by Django 4.2.7 on 2023-12-16 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_one',
            new_name='created_on',
        ),
    ]
