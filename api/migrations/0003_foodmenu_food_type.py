# Generated by Django 3.2.10 on 2024-07-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_aboutus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmenu',
            name='food_type',
            field=models.CharField(choices=[('VEG', 'Vegetarian'), ('NON_VEG', 'Non-Vegetarian')], default='Veg', max_length=7),
        ),
    ]
