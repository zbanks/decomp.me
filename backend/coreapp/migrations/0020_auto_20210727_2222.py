# Generated by Django 3.2.4 on 2021-07-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0019_auto_20210726_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='scratch',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='scratch',
            name='source_code',
            field=models.TextField(blank=True),
        ),
    ]
