# Generated by Django 5.1 on 2024-08-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answer',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='quiz',
            name='desc',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_1',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_2',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_3',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_4',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='quiz',
            name='status',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
