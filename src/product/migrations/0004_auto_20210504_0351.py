# Generated by Django 3.2 on 2021-05-04 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0003_auto_20210504_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Product Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Product Category'),
        ),
    ]
