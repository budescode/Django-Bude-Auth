# Generated by Django 2.2 on 2020-11-21 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budesocial', '0006_auto_20201121_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budesocialmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
