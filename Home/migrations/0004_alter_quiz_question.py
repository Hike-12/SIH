# Generated by Django 5.1 on 2024-08-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_quiz_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
