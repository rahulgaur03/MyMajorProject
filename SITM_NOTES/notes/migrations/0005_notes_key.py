# Generated by Django 3.1.4 on 2021-04-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_notes_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='key',
            field=models.CharField(default='', max_length=122),
        ),
    ]