# Generated by Django 4.2.7 on 2023-12-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_bode_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
