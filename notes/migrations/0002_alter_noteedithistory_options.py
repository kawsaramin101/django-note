# Generated by Django 4.2 on 2024-03-17 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noteedithistory',
            options={'ordering': ['-created']},
        ),
    ]
