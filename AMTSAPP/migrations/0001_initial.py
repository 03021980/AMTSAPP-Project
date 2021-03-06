# Generated by Django 2.2.12 on 2021-10-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('scourse', models.CharField(max_length=30)),
                ('sphonenumber', models.IntegerField()),
                ('sage', models.IntegerField()),
                ('saddress', models.CharField(max_length=30)),
                ('semail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('ccourse', models.CharField(max_length=30)),
                ('cyear', models.IntegerField()),
                ('cphoto', models.CharField(max_length=30)),
                ('cfees', models.CharField(max_length=30)),
            ],
        ),
    ]
