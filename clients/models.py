from django.contrib.auth.models import Group, User
from django.core.validators import RegexValidator
from django.db import models

REGEX_PHONE = RegexValidator(regex='^\+7\d{10}$', message='Incorrect phone number format')
REGEX_VK_ID = RegexValidator(regex='^id\d{1,}$', message='Invalid vk id')
GENDER = (
    ('М', 'Мужской'),
    ('Ж', 'Женский'),
)


class Client(models.Model):
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    special_client = models.TextField(max_length=512, blank=True)
    email = models.EmailField(blank=True)
    phone_number_1 = models.CharField(max_length=12, validators=[REGEX_PHONE], blank=True)
    phone_number_2 = models.CharField(max_length=12, validators=[REGEX_PHONE], blank=True)
    phone_number_non_format = models.CharField(max_length=100, blank=True)
    phone_number_ext = models.CharField(max_length=100, blank=True)
    vk_id = models.CharField(max_length=14, validators=[REGEX_VK_ID], blank=True)
    time_to_call = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField(blank=True, null=True)
    specialists = models.ManyToManyField('auth.User', related_name='clients_reception',)
    registrar = models.ForeignKey('auth.User', related_name='clients_registered', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
