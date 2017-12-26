from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from clients.models import Client
from clients.permissions import DjangoModelPermissionsOrIsClientSpecialist
from clients.serializers import ClientSerializer, UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (DjangoModelPermissionsOrIsClientSpecialist,)

    def perform_create(self, serializer):
        serializer.save(registrar=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Client.objects.filter(specialists=request.user)
        serializer = ClientSerializer(queryset, many=True, context={'request': request})
        if request.user in User.objects.filter(groups__name='Specialists'):
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
