# Generated by Django 3.1 on 2020-09-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_libbookacquired'),
    ]

    operations = [
        migrations.AddField(
            model_name='libuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]