# Generated by Django 3.2.4 on 2021-08-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210825_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='phone_numbers',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
