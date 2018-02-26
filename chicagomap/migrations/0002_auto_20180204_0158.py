# Generated by Django 2.0.2 on 2018-02-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicagomap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhoods',
            name='pri_neigh',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='neighborhoods',
            name='sec_neigh',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='neighborhoods',
            name='shape_area',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='neighborhoods',
            name='shape_len',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='precincts',
            name='full_text',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='precincts',
            name='precinct',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='precincts',
            name='shape_area',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='precincts',
            name='shape_len',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='precincts',
            name='ward',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='commarea',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='commarea_n',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='countyfp10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='geoid10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='name10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='namelsad10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='notes',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='statefp10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tracts',
            name='tractce10',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wards',
            name='shape_area',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wards',
            name='shape_leng',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='wards',
            name='ward',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zips',
            name='objectid',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zips',
            name='shape_area',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zips',
            name='shape_len',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='zips',
            name='zip',
            field=models.CharField(max_length=32),
        ),
    ]