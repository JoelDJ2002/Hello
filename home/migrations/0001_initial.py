# Generated by Django 4.0.5 on 2022-07-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('phone', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
