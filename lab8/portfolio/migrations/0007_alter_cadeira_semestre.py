# Generated by Django 4.0.4 on 2022-05-18 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_pessoa_linkpaginalinkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='semestre',
            field=models.IntegerField(choices=[(1, '1º Semestre'), (2, '2º Semestre')], default=1),
        ),
    ]
