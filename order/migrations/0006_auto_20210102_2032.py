# Generated by Django 2.2.5 on 2021-01-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210102_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='toltalquantity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='totalprice',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True),
        ),
    ]
