
from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Room,Book,Contact,Price
from datetime import datetime, timedelta
from datetime import tzinfo
import time



# Create your views here.
def index(request):
	
	room_category = request.GET.get('room_category')
	check_in = request.GET.get('check_in')
	check_out = request.GET.get('check_out')
	if Room.objects.filter(R_category=room_category,available=True).exists() == True:
		messages.info(request,"Room is available")
	else:
		messages.info(request,"Room is not available")
				
	return render(request, 'index.html')
	
def restaurant(request):
    return render(request, 'Restaurant.html')

def book(request):

	if request.method == "POST":	
		roomsdetails = request.POST.get('roomsdetails',"")
		adultsdetails = request.POST.get('adultsdetails',"")
		childrendetails = request.POST.get('childrendetails',"")
		checkindetails = request.POST.get('checkindetails',"")
		checkoutdetails = request.POST.get('checkoutdetails',"")
		namedetails = request.POST.get('namedetails',"")
		phonedetails = request.POST.get('phonedetails',"")
		emaildetails = request.POST.get('emaildetails',"")
		moredetails = request.POST.get('moredetails',"")
		if Room.objects.filter(R_category=roomsdetails,available=True).exists()  == True:
			book = Book(
				roomsdetails=roomsdetails,
				adultsdetails=adultsdetails,
				childrendetails=childrendetails,
				checkindetails=checkindetails,
				checkoutdetails=checkoutdetails,
				namedetails=namedetails,
				phonedetails=phonedetails,
				emaildetails=emaildetails,
				moredetails=moredetails)
			book.save()
			price = Price.objects.filter(R_category=roomsdetails)
			messages.success(request,"Booked successfully")
			return render(request, 'payment.html', {'roomsdetails': roomsdetails , 'emaildetails':emaildetails,
					'namedetails':namedetails,'phonedetails':phonedetails,
					'checkindetails':checkindetails,'price':price})
			
	return render(request, 'Booking.html')

def rooms(request):
    return render(request, 'Rooms.html')

def contact(request):

	if request.method == "POST":
		
		email = request.POST.get('email',"")
		first_name = request.POST.get('first_name',"")
		last_name = request.POST.get('last_name',"")
		phone_number = request.POST.get('phone_number',"")
		country = request.POST.get('country',"")
		comment_type = request.POST.get('comment_type',"")
		feedback = request.POST.get('feedback',"")
		contact = Contact(email=email,
			first_name=first_name,
			last_name=last_name,
			phone_number=phone_number,
			country=country,
			comment_type=comment_type,
			feedback=feedback)
		contact.save()
	messages.info(request,"Thanks for your comments")

	return render(request, 'contact.html')

def location(request):
    return render(request, 'Location.html')

def about(request):
    return render(request, 'About.html')

def payment(request):
	return render(request,'payment.html')

def paymentdone(request):
	return render(request,'paymentdone.html')