# Generated by Django 2.2.5 on 2020-12-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProduct', '0016_variants_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variants',
            name='gender',
        ),
    ]
