# Generated by Django 2.1.dev20180205164247 on 2018-06-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20180627_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
