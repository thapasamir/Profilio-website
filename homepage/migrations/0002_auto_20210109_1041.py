# Generated by Django 3.1.4 on 2021-01-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1', models.CharField(max_length=1000, null=True)),
                ('description2', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='addprof',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
