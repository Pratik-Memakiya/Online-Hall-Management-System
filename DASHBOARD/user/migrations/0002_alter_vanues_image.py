# Generated by Django 3.2 on 2021-04-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vanues',
            name='Image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
