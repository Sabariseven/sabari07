# Generated by Django 2.2.4 on 2019-09-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('submitted', 'SUBMITTED'), ('accepted', 'ACCEPTED'), ('rejected', 'REJECTED')], default='submitted', max_length=20),
        ),
    ]
