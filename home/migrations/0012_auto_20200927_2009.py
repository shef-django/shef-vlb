# Generated by Django 3.1 on 2020-09-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_libuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libbookacquired',
            name='name',
        ),
        migrations.DeleteModel(
            name='LibUser',
        ),
    ]