# Generated by Django 5.1.3 on 2024-12-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20200608_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
