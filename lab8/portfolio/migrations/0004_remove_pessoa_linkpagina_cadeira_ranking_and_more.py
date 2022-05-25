# Generated by Django 4.0.4 on 2022-05-18 18:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_cadeira_semestre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='linkPagina',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='ranking',
            field=models.IntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')], default=3),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='linkPaginaLinkedin',
            field=models.URLField(default=False),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='linkPaginaLusofona',
            field=models.URLField(default=False),
        ),
        migrations.AddField(
            model_name='projeto',
            name='cadeira',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.cadeira'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='participantes',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='ects',
            field=models.IntegerField(default=6, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=20)]),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='semestre',
            field=models.IntegerField(choices=[(1, '1º Semestre'), (2, '2º Semestre'), (3, 'Anual')], default=1),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='topicosAbordados',
            field=models.CharField(default=False, max_length=1024),
        ),
    ]