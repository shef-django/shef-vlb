# Generated by Django 3.1 on 2020-08-30 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_delete_libbookacquired'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibBookAcquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Alloted', 'Alloted'), ('Rejected', 'Rejected')], max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Stu_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.libuser')),
                ('book_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.libbook')),
            ],
        ),
    ]
