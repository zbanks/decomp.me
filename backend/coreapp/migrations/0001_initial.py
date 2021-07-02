# Generated by Django 3.2.4 on 2021-07-01 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('repo_url', models.URLField()),
                ('discord_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn_text', models.TextField()),
                ('visits', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.project')),
            ],
        ),
    ]