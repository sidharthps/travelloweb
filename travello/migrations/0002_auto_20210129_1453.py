# Generated by Django 3.1.5 on 2021-01-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='destination',
            field=models.TextField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='image',
            field=models.ImageField(default=11, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='name',
            field=models.CharField(default=22, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=33),
            preserve_default=False,
        ),
    ]
