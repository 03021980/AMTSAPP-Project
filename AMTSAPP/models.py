from django.db import models
from django.utils import timezone

# Create your models here.
class LoginModel(models.Model):
	sname=models.CharField(max_length=30)
	scourse=models.CharField(max_length=30)
	sphonenumber=models.IntegerField()
	sage=models.IntegerField()
	saddress=models.CharField(max_length=30)
	semail=models.CharField(max_length=30)

	def __str__(self):
		return self.sname   
	
	class Meta:
		db_table = 'AMTSAPP'
        # Add verbose name
		verbose_name = 'STUDENT MODEL'

class StudentModel(models.Model):
	cname=models.CharField(max_length=30)
	ccourse=models.CharField(max_length=30)
	cyear=models.IntegerField()
	cphoto=models.FileField(max_length=30)
	cfees=models.FileField(max_length=30)

class JobModel(models.Model):
	jname=models.CharField(max_length=30)
	jaddress=models.CharField(max_length=30)
	jletter=models.FileField(max_length=30)

class SeniorCitizenModel(models.Model):
	scname=models.CharField(max_length=30)
	scage=models.IntegerField()