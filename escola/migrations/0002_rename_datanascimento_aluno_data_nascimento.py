# Generated by Django 3.2.7 on 2021-09-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='dataNascimento',
            new_name='data_nascimento',
        ),
    ]