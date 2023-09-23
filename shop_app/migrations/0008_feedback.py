# Generated by Django 4.2.1 on 2023-09-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
