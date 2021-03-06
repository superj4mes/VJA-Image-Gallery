# Generated by Django 3.2.8 on 2021-10-13 21:46

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 13, 21, 46, 37, 931580))),
                ('ispublic', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.upload_gallery_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'gif', 'png'])])),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('img_description', models.CharField(blank=True, default='', max_length=200)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.gallery')),
            ],
        ),
    ]
