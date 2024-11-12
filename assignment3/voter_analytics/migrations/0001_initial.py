# Generated by Django 5.1.1 on 2024-11-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=100)),
                ('apartment_number', models.CharField(blank=True, max_length=10, null=True)),
                ('zip_code', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('date_of_registration', models.DateField()),
                ('party_affiliation', models.CharField(max_length=10)),
                ('precinct_number', models.CharField(max_length=10)),
                ('voted_2020_state', models.BooleanField(default=False)),
                ('voted_2021_town', models.BooleanField(default=False)),
                ('voted_2021_primary', models.BooleanField(default=False)),
                ('voted_2022_general', models.BooleanField(default=False)),
                ('voted_2023_town', models.BooleanField(default=False)),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]
