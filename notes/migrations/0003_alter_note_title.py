# Generated by Django 4.2 on 2024-03-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_noteedithistory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
