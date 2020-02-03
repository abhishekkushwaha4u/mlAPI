# Generated by Django 3.0.3 on 2020-02-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_handling', '0002_auto_20200203_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_name',
            name='classifier_file',
            field=models.FileField(default=1, upload_to='ClassifierFile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='app_name',
            name='url',
            field=models.URLField(blank=True, unique=True),
        ),
    ]
