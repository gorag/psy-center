# Generated by Django 2.0 on 2017-12-06 08:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('special_client', models.TextField(blank=True, max_length=512)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number_1', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Incorrect phone number format', regex='^\\+7\\d{10}$')])),
                ('phone_number_2', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Incorrect phone number format', regex='^\\+7\\d{10}$')])),
                ('phone_number_non_format', models.CharField(blank=True, max_length=100)),
                ('phone_number_ext', models.CharField(blank=True, max_length=100)),
                ('vk_id', models.CharField(blank=True, max_length=14, validators=[django.core.validators.RegexValidator(message='Invalid vk id', regex='^id\\d{1,}$')])),
                ('time_to_call', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
                ('registrar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='clients_registered', to=settings.AUTH_USER_MODEL)),
                ('specialists', models.ManyToManyField(related_name='clients_reception', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]