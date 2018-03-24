from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for User"""
	web = models.CharField(max_length=300)
	passwd = models.CharField(max_length=30)
	count = models.CharField(max_length=50)
	note = models.CharField(max_length=300)
		