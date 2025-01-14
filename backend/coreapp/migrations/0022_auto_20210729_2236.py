# Generated by Django 3.2.4 on 2021-07-29 13:36

import coreapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0021_rename_assembly_asm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compilation',
            old_name='assembly',
            new_name='asm',
        ),
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('object', models.FilePathField(path=coreapp.models.asm_objects_path)),
                ('compiler_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.compilerconfiguration')),
                ('source_asm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.asm')),
            ],
        ),
    ]
