# Generated by Django 4.0.2 on 2022-06-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0009_resume_dpassingyear_resume_dbranch_resume_dcourse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='univercity',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]