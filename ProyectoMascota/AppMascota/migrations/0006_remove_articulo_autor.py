# Generated by Django 4.1 on 2022-10-18 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMascota', '0005_articulo_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='autor',
        ),
    ]
