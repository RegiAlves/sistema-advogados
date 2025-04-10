# Generated by Django 5.2 on 2025-04-06 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('processos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('local', models.CharField(blank=True, max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('processo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processos.processo')),
            ],
        ),
    ]
