# Generated by Django 4.2.4 on 2023-09-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_register_accno_alter_register_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.IntegerField(verbose_name='1'),
        ),
    ]
