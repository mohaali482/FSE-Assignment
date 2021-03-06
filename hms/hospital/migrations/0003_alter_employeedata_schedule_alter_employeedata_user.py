# Generated by Django 4.0.1 on 2022-01-15 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0002_schedule_employeedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.schedule', verbose_name='Schedule'),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
