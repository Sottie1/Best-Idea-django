# Generated by Django 4.2.3 on 2023-07-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='works/photos'),
        ),
    ]
