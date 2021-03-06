# Generated by Django 3.2.6 on 2021-10-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20211006_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='Student',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='Teacher',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='subjectattendence',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='subjectclass',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='subjectmarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='subjectscore',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
