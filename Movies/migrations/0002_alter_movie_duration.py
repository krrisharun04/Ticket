# Generated by Django 3.2.12 on 2022-05-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.BooleanField(),
        ),
    ]
