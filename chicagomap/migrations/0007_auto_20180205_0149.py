# Generated by Django 2.0.2 on 2018-02-05 01:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chicagomap', '0006_auto_20180205_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='TractToPrecinct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='WardToTract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ZipToPrecinct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ZipToTract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ZipToWard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='precinct',
            name='neighborhoods',
            field=models.ManyToManyField(through='chicagomap.NeighborhoodToPrecinct', to='chicagomap.Neighborhood'),
        ),
        migrations.AddField(
            model_name='tract',
            name='neighborhoods',
            field=models.ManyToManyField(through='chicagomap.NeighborhoodToTract', to='chicagomap.Neighborhood'),
        ),
        migrations.AddField(
            model_name='ward',
            name='neighborhoods',
            field=models.ManyToManyField(through='chicagomap.NeighborhoodToWard', to='chicagomap.Neighborhood'),
        ),
        migrations.AddField(
            model_name='zip',
            name='neighborhoods',
            field=models.ManyToManyField(through='chicagomap.NeighborhoodToZip', to='chicagomap.Neighborhood'),
        ),
        migrations.AddField(
            model_name='ziptoward',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Ward'),
        ),
        migrations.AddField(
            model_name='ziptoward',
            name='zip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='ziptotract',
            name='tract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='ziptotract',
            name='zip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='ziptoprecinct',
            name='precinct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Precinct'),
        ),
        migrations.AddField(
            model_name='ziptoprecinct',
            name='zip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='wardtotract',
            name='tract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='wardtotract',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Ward'),
        ),
        migrations.AddField(
            model_name='tracttoprecinct',
            name='precinct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Precinct'),
        ),
        migrations.AddField(
            model_name='tracttoprecinct',
            name='tract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='precinct',
            name='tracts',
            field=models.ManyToManyField(through='chicagomap.TractToPrecinct', to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='precinct',
            name='zips',
            field=models.ManyToManyField(through='chicagomap.ZipToPrecinct', to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='tract',
            name='precincts',
            field=models.ManyToManyField(through='chicagomap.TractToPrecinct', to='chicagomap.Precinct'),
        ),
        migrations.AddField(
            model_name='tract',
            name='wards',
            field=models.ManyToManyField(through='chicagomap.WardToTract', to='chicagomap.Ward'),
        ),
        migrations.AddField(
            model_name='tract',
            name='zips',
            field=models.ManyToManyField(through='chicagomap.ZipToTract', to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='ward',
            name='tracts',
            field=models.ManyToManyField(through='chicagomap.WardToTract', to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='ward',
            name='zips',
            field=models.ManyToManyField(through='chicagomap.ZipToWard', to='chicagomap.Zip'),
        ),
        migrations.AddField(
            model_name='zip',
            name='precincts',
            field=models.ManyToManyField(through='chicagomap.ZipToPrecinct', to='chicagomap.Precinct'),
        ),
        migrations.AddField(
            model_name='zip',
            name='tracts',
            field=models.ManyToManyField(through='chicagomap.ZipToTract', to='chicagomap.Tract'),
        ),
        migrations.AddField(
            model_name='zip',
            name='wards',
            field=models.ManyToManyField(through='chicagomap.ZipToWard', to='chicagomap.Ward'),
        ),
    ]