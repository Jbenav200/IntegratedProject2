# Generated by Django 2.1.7 on 2019-04-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20190408_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='id',
            field=models.IntegerField(auto_created=1, primary_key=1, serialize=False),
        ),
    ]