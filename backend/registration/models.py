from django.db import models


class Registration(models.Model):
	name = models.CharField(max_length=50)
	email_id = models.CharField(max_length=30, unique=True)
	phone_number = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return self.name +"("+self.email_id+")"