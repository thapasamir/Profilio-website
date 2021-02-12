from django.db import models

# Create your models here.
class AddProf(models.Model):
	name = models.CharField(max_length=10,null=False)
	description = models.CharField(max_length=1000,null=True)
	thumnail = models.ImageField(upload_to="documents/")

	def __str__(self):
		return self.name


class about(models.Model):
	description1 = models.CharField(max_length=1000,null=True)
	description2 = models.CharField(max_length=1000,null=True)
