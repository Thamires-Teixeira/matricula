# Generated by Django 4.2.2 on 2023-07-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aluno", "0002_rename_matricula_aluno"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="alunos"),
        ),
        migrations.AddField(
            model_name="aluno",
            name="valor",
            field=models.FloatField(blank=True, null=True),
        ),
    ]