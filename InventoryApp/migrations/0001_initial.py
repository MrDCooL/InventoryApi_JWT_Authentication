# Generated by Django 5.1.1 on 2025-06-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('barcode', models.IntegerField()),
            ],
        ),
    ]
