# Generated by Django 3.1.3 on 2020-12-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20201203_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]