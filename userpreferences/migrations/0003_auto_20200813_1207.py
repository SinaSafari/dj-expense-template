# Generated by Django 3.1 on 2020-08-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0002_auto_20200811_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='currency',
            field=models.CharField(blank=True, default='USD - United States Dollar', max_length=255, null=True),
        ),
    ]