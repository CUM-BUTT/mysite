# Generated by Django 3.0.2 on 2020-05-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('card_num', models.CharField(max_length=16)),
                ('password', models.IntegerField()),
                ('cvc', models.IntegerField()),
            ],
        ),
    ]
