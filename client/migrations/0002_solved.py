# Generated by Django 4.2.3 on 2023-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('causeofcomplaint', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]