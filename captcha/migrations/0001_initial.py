# Generated by Django 3.1.1 on 2020-09-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('captcha', models.CharField(max_length=50)),
            ],
        ),
    ]
