# Generated by Django 4.2 on 2024-05-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0004_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='chef_image',
            field=models.ImageField(default=None, upload_to='shef_image/(%Y-%m-%d)'),
            preserve_default=False,
        ),
    ]
