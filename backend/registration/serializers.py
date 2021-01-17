from rest_framework import serializers
from .models import Registration


class registrationSerializers(serializers.ModelSerializer):
	class Meta:
		model = Registration
		fields = ('id', 'name', 'email_id', 'phone_number')