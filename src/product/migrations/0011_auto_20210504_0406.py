# Generated by Django 3.2 on 2021-05-04 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210504_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDBrand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PRDCategory',
        ),
    ]
