# Generated by Django 3.2.7 on 2022-04-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='application_deadline',
            field=models.DateField(),
        ),
    ]
