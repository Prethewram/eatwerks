# Generated by Django 4.2.7 on 2024-07-10 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='title',
        ),
    ]