from django.contrib.auth.hashers import make_password
from django.contrib.auth.management import create_permissions
from django.db import migrations

GROUP_ADMINISTRATORS = 'Administrators'
GROUP_REGISTRARS = 'Registrars'
GROUP_SPECIALISTS = 'Specialists'

DEFAULT_ADMIN_PASSWORD = make_password('admin')


def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def create_groups(apps, schema_editor):
    Group = apps.get_registered_model('auth', 'Group')
    Permission = apps.get_registered_model('auth', 'Permission')
    User = apps.get_registered_model('auth', 'User')

    permissions_all = Permission.objects.all()
    permissions_clients_all = Permission.objects.filter(codename__endswith='client')

    group_administrators = Group(name=GROUP_ADMINISTRATORS)
    group_registrars = Group(name=GROUP_REGISTRARS)
    group_specialists = Group(name=GROUP_SPECIALISTS)

    group_administrators.save()
    group_registrars.save()
    group_specialists.save()

    group_administrators.permissions.set(permissions_all)
    group_registrars.permissions.set(permissions_clients_all)

    admin = User(
        username='admin',
        email='admin@example.com',
        password=DEFAULT_ADMIN_PASSWORD,
        is_superuser=True,
        is_staff=True,
    )
    admin.save()
    admin.groups.add(group_administrators)

    default_user_password = make_password('1')
    users = [
        {'username': 'registrar1', 'group': group_registrars},
        {'username': 'registrar2', 'group': group_registrars},
        {'username': 'spec1', 'group': group_specialists},
        {'username': 'spec2', 'group': group_specialists},
    ]

    for user in users:
        created_user = User(username=user.get('username'), password=default_user_password)
        created_user.save()
        created_user.groups.add(user.get('group'))


class Migration(migrations.Migration):
    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_permissions),
        migrations.RunPython(create_groups),
    ]
