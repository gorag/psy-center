from django.contrib.auth.models import User
from rest_framework import permissions


class DjangoModelPermissionsOrIsClientSpecialist(permissions.DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        if request.user in User.objects.filter(groups__name="Specialists"):
            if request.user in obj.specialists.all():
                return True
            else:
                return False
        return super().has_object_permission(request, view, obj)
