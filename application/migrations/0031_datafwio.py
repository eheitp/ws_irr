# Generated by Django 3.2.14 on 2023-05-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0030_auto_20230507_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFwiO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffmc', models.FloatField()),
                ('dmc', models.FloatField()),
                ('dc', models.FloatField()),
                ('isi', models.FloatField()),
                ('bui', models.FloatField()),
                ('fwi', models.FloatField()),
                ('Time_Stamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]