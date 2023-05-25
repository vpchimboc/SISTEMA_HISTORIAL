# Generated by Django 4.2.1 on 2023-05-23 03:11

import app.models
import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='11111-fghjk', editable=False, populate_from=app.models.generar_slug),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha_medica',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='11111-fghjk', editable=False, populate_from=app.models.generar_slug),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='11111-fghjk', editable=False, populate_from=app.models.generar_slug),
            preserve_default=False,
        ),
    ]