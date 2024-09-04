# Generated by Django 5.1 on 2024-09-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_short_hero_day_event_hero_day_event_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='None', max_length=50)),
                ('case_study', models.TextField(default='None')),
                ('status', models.BooleanField(default=False)),
                ('solution', models.TextField(default='None')),
            ],
        ),
    ]
