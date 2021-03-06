# Generated by Django 3.0.8 on 2020-10-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helmet',
            fields=[
                ('helmet_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('image', models.FileField(upload_to='static/images/ground/')),
            ],
            options={
                'db_table': 'helmet',
            },
        ),
    ]
