# Generated by Django 3.0.8 on 2020-07-20 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArchiSite', '0003_auto_20200720_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default=None, upload_to='images/blog')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image1',
            field=models.ImageField(default=None, upload_to='images/portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(default=None, upload_to='images/portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(default=None, upload_to='images/portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image4',
            field=models.ImageField(default=None, upload_to='images/portfolio'),
        ),
    ]
