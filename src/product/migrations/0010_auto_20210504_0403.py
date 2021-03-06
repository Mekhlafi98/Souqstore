# Generated by Django 3.2 on 2021-05-04 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0009_auto_20210504_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Product Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Product Category'),
            preserve_default=False,
        ),
    ]
