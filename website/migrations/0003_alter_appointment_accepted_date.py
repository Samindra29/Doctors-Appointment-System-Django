# Generated by Django 3.2.9 on 2021-12-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_appointment_accepted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='accepted_date',
            field=models.DateField(default=True),
        ),
    ]
