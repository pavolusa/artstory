# Generated by Django 2.1.3 on 2018-11-08 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artstory', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
