# Generated by Django 3.0.8 on 2020-08-01 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditationascensionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=models.TextField(),
        ),
    ]
