# Generated by Django 4.2.20 on 2025-05-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_food_date_remove_food_meal_food_calories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='foods',
            field=models.ManyToManyField(to='main_app.food'),
        ),
    ]
