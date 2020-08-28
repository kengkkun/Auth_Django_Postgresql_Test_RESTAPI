# Generated by Django 3.1 on 2020-08-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('cleaned', models.CharField(max_length=100)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]