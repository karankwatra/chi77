# Generated by Django 2.0.2 on 2018-03-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicagomap', '0007_auto_20180205_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tract',
            name='id',
        ),
        migrations.AlterField(
            model_name='tract',
            name='name10',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
