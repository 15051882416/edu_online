# Generated by Django 3.0.5 on 2020-04-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orginfo',
            name='course_num',
        ),
    ]
