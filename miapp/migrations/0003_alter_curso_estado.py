# Generated by Django 4.1 on 2022-08-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estado',
            field=models.TextField(),
        ),
    ]
