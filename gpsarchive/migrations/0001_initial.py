# Generated by Django 3.0.8 on 2020-08-22 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='gpxfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('callsign', models.CharField(max_length=100, verbose_name='Callsign')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gpx_file', models.FileField(upload_to='gpxstorage/')),
            ],
        ),
        migrations.CreateModel(
            name='gpxtrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=200, verbose_name='Opis')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('gpx_file', models.FileField(upload_to='gpxstorage/', verbose_name='Plik GPX')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='gpxcompare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=200, verbose_name='Opis')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('gpx_file_track', models.FileField(upload_to='gpxstorage/', verbose_name='Pierwszy Plik')),
                ('gpx_file_route', models.FileField(upload_to='gpxstorage/', verbose_name='Drugi Plik')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
