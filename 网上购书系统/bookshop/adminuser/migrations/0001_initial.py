# Generated by Django 2.1.1 on 2019-02-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password_hash', models.TextField()),
                ('root', models.IntegerField()),
            ],
        ),
    ]
