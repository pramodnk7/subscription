from django.shortcuts import render
from rest_framework import generics
from .serializers import registrationSerializers
from .models import Registration


class registrationListView(generics.ListAPIView):
	queryset = Registration.objects.all()
	serializer_class = registrationSerializers


class registrationDetailView(generics.RetrieveAPIView):
	queryset = Registration.objects.all()
	serializer_class = registrationSerializers
	print(queryset)

