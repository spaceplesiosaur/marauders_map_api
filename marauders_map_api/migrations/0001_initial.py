# Generated by Django 3.0.6 on 2020-05-21 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60000)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60000, unique=True)),
                ('current_occupants', models.ManyToManyField(to='marauders_map_api.Character')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60000)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='head', to='marauders_map_api.Character')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marauders_map_api.Location')),
                ('members', models.ManyToManyField(related_name='house', to='marauders_map_api.Character')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ally', models.BooleanField(default=True)),
                ('is_enemy', models.BooleanField(default=False)),
                ('from_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_connections', to='marauders_map_api.Character')),
                ('to_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_connections', to='marauders_map_api.Character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='connections',
            field=models.ManyToManyField(related_name='_character_connections_+', through='marauders_map_api.Connection', to='marauders_map_api.Character'),
        ),
    ]
