from django.db import models

# Create your models here.
class Employees(models.Model):
	FirstName=models.CharField(max_length=250,null=True)
	Address=models.TextField(null=True)
	LastName=models.CharField(max_length=250,null=True)
	EmailAddress=models.CharField(max_length=250,null=True)
	Date=models.DateField(null=True)
	CreatedDate=models.DateTimeField(auto_now_add=True)
	ModiefiedTime=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.FirstName



class Book(models.Model):
	bookname=models.CharField(max_length=250,unique=True,null=True)
	employee=models.ForeignKey(Employees,unique=True,on_delete=models.CASCADE)
	def __str__(self):
		return self.bookname






