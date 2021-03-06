# Generated by Django 2.1.3 on 2018-11-22 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50)),
                ('pushover_user_key', models.CharField(max_length=50)),
                ('pushover_app_key', models.CharField(max_length=50)),
                ('slack_room_name', models.CharField(max_length=50)),
                ('prowl_api_key', models.CharField(blank=True, max_length=50)),
                ('prowl_application', models.CharField(blank=True, max_length=256)),
                ('prowl_url', models.CharField(blank=True, max_length=512)),
                ('rocket_webhook_url', models.CharField(blank=True, max_length=512)),
                ('hipchat_room_name', models.CharField(max_length=100)),
                ('hipchat_room_url', models.CharField(max_length=100)),
                ('send_resolve_enabled', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
