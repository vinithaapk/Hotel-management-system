from django.db import models
from django.conf import settings
from datetime import datetime
from datetime import tzinfo

# Create your models here.
class Room(models.Model):
	
	room_category = (
		('SINGLE AC', 'SINGLE AC'),
		('SINGLE NON-AC','SINGLE NON-AC'),
		('DOUBLE AC',' DOUBLE AC'),
		('DOUBLE NON-AC','DOUBLE NON-AC'),
		('TRIPLE AC', 'TRIPLE AC'),
		('TRIPLE NON-AC','TRIPLE NON-AC'),
		('DOUBLE ROOM AC','DOUBLE ROOM AC'),
		('DOUBLE ROOM NON-AC','DOUBLE ROOM NON-AC'),
		('FAMILY AC','FAMILY AC'),
		('KING AC','KING AC'),
		('DOUBLE-DOUBLE AC','DOUBLE-DOUBLE AC'),
		('STUDIO','STUDIO'),
		('PRESIDENT SUITE','PRESIDENT SUITE')
	)
	R_category = models.CharField(max_length=100,choices=room_category)
	room_number = models.IntegerField()
	capacity = models.IntegerField(default='0')
	price = models.CharField(max_length=30,default='0')
	available = models.BooleanField(default="False")

	def __str__(self):
		return f'{self.room_number}  - {self.R_category} with the capacity of {self.capacity} people. Price is Rs.{self.price}  '

class Price(models.Model):
	
	room_category = (
		('SINGLE AC', 'SINGLE AC'),
		('SINGLE NON-AC','SINGLE NON-AC'),
		('DOUBLE AC',' DOUBLE AC'),
		('DOUBLE NON-AC','DOUBLE NON-AC'),
		('TRIPLE AC', 'TRIPLE AC'),
		('TRIPLE NON-AC','TRIPLE NON-AC'),
		('DOUBLE ROOM AC','DOUBLE ROOM AC'),
		('DOUBLE ROOM NON-AC','DOUBLE ROOM NON-AC'),
		('FAMILY AC','FAMILY AC'),
		('KING AC','KING AC'),
		('DOUBLE-DOUBLE AC','DOUBLE-DOUBLE AC'),
		('STUDIO','STUDIO'),
		('PRESIDENT SUITE','PRESIDENT SUITE')
	)
	R_category = models.CharField(max_length=100,choices=room_category)
	price = models.CharField(max_length=30,default='0')

	def __str__(self):
		return f'{self.price}'

class Book(models.Model):

	roomsdetails = models.CharField(max_length=50)
	adultsdetails = models.IntegerField(default='0')
	childrendetails = models.IntegerField(default='0')
	checkindetails = models.DateField(blank=True, null=True)
	checkoutdetails = models.DateField(blank=True, null=True)
	namedetails = models.CharField(max_length=50, default='test')
	phonedetails = models.CharField(max_length=12, default='test')
	emaildetails = models.CharField(max_length=50,  default='test')
	moredetails = models.CharField(max_length=50,  default='nothing')
	
	def __str__(self):	
		return f'{self.namedetails} has booked {self.roomsdetails} from {self.checkindetails} to {self.checkoutdetails}'

class Contact(models.Model):
	country = (('India','India'),
				('France','France'),
				('Germany','Germany'),
				('Italy','Italy'),
				('Japan','Japan'),
				('Russia','Russia'),
				('United Kingdom','UK'),
				('United States','US'))

	comment_type = (('Request','Request'),
				('Comment','Comment'))
	
	email = models.CharField(max_length=30, default='test')
	first_name = models.CharField(max_length=20, default='test')
	last_name = models.CharField(max_length=20, default='test',)
	phone_number = models.CharField(max_length=20, default='number')
	country = models.CharField(max_length=20, choices=country)
	comment_type = models.CharField(max_length=20, choices=comment_type)
	feedback = models.CharField(max_length=300, default='test')

	def __str__(self):
		return f'{self.first_name} has made a {self.comment_type} - {self.feedback} from {self.country}'
