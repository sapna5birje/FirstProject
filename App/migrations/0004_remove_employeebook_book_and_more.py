# Generated by Django 4.0.4 on 2022-05-01 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_employeeonetomany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeebook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='employeebook',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeonetomany',
            name='book',
        ),
        migrations.RemoveField(
            model_name='employeeonetomany',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='employeeBook',
        ),
        migrations.DeleteModel(
            name='employeeonetomany',
        ),
    ]