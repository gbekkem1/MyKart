# Generated by Django 5.1.6 on 2025-03-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
