# Generated by Django 4.2.1 on 2023-07-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittel', models.CharField(max_length=35)),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
    ]
