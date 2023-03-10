# Generated by Django 3.2 on 2023-01-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('category', models.CharField(db_column='category', max_length=255)),
                ('aver_price', models.IntegerField(db_column='aver_price', max_length=11)),
                ('arrival_time', models.IntegerField(db_column='arrival_time', max_length=11)),
                ('call_number', models.CharField(db_column='call_number', max_length=255)),
                ('location', models.CharField(db_column='location', max_length=255)),
            ],
            options={
                'db_table': 'store_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_column='user_id', max_length=11)),
                ('store_name', models.CharField(db_column='store_name', max_length=255)),
                ('store_rating', models.IntegerField(db_column='store_rating', max_length=11)),
                ('comment', models.CharField(db_column='comment', max_length=255)),
            ],
            options={
                'db_table': 'store_rating',
                'managed': False,
            },
        ),
    ]
