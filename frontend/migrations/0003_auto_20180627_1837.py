# Generated by Django 2.1.dev20180205164247 on 2018-06-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20180626_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='adjunto',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(),
        ),
    ]
