# Generated by Django 4.0.5 on 2022-08-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_contacts_email_alter_contacts_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=80),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='usn',
            field=models.CharField(max_length=10),
        ),
    ]
