# Generated by Django 5.1.2 on 2024-10-20 20:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criterios', to='ux.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionPuntaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(choices=[(1, 'Muy Deficiente'), (2, 'Deficiente'), (3, 'Aceptable'), (4, 'Buena'), (5, 'Excelente')])),
                ('descripcion', models.TextField()),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descripciones', to='ux.criterio')),
            ],
        ),
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubricas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(choices=[(1, 'Muy Deficiente'), (2, 'Deficiente'), (3, 'Aceptable'), (4, 'Buena'), (5, 'Excelente')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ux.categoria')),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ux.criterio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to=settings.AUTH_USER_MODEL)),
                ('rubrica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to='ux.rubrica')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='rubrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='ux.rubrica'),
        ),
    ]
