# Generated by Django 3.1.1 on 2020-10-14 06:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TodoList', '0002_auto_20201013_1329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='List',
        ),
    ]