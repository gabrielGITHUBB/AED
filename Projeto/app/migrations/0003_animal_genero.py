# Generated by Django 5.0.6 on 2024-08-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_animal_descricao_completa'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='genero',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
