# Generated by Django 5.1.1 on 2024-11-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=20),
        ),
    ]
