# Generated by Django 4.0.4 on 2022-05-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('cumpleanos', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('cumpleanos', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Familiar3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('cumpleanos', models.DateField()),
            ],
        ),
    ]
