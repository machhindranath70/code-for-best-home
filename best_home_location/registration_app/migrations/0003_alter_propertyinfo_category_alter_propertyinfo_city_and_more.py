# Generated by Django 5.1 on 2025-03-31 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0002_propertyinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyinfo',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='full_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='photo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='reviews_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='reviews_tags',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='site',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='street_view',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='subtypes',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='propertyinfo',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
