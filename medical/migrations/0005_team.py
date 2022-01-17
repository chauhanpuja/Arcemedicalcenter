# Generated by Django 3.2.5 on 2022-01-15 15:35

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_auto_20220115_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('speciality', models.CharField(default='', max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('image', models.ImageField(default='', upload_to='image')),
            ],
        ),
    ]
