# Generated by Django 3.2.4 on 2021-07-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0014_auto_20210705_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compiler',
            name='compile_cmd',
            field=models.CharField(max_length=1000),
        ),
    ]
