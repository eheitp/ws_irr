# Generated by Django 3.2.14 on 2023-05-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0031_datafwio'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='d',
            field=models.IntegerField(null=True),
        ),
    ]