from django.contrib.auth.models import User
from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    registrar = serializers.ReadOnlyField(source='registrar.username')

    class Meta:
        model = Client
        fields = (
            'url', 'id', 'last_name', 'first_name', 'middle_name', 'special_client', 'email', 'phone_number_1',
            'phone_number_2', 'phone_number_non_format', 'phone_number_ext', 'vk_id', 'time_to_call',
            'gender', 'date_of_birth', 'specialists', 'registrar'
        )


class UserSerializer(serializers.ModelSerializer):
    clients_registered = serializers.HyperlinkedRelatedField(many=True, view_name='client-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'clients_registered', 'clients_reception'
        )
