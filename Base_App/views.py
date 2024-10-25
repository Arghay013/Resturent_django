from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemList, Items, AboutUs, Feedback, BookTable

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list, 'review': review})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})

def ManuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})

def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '').strip()
        phone_number = request.POST.get('user_phone_number', '').strip()
        email = request.POST.get('user_email', '').strip()
        total_person = request.POST.get('total_person', '').strip()
        booking_date = request.POST.get('booking_date', '').strip()
        
        if name and phone_number and email and total_person and booking_date:
            data = BookTable(Name=name, Phone_number=phone_number, Email=email, Total_person=total_person, Booking_date=booking_date)
            data.save()
            return render(request, 'book_table.html', {'success': True})

    return render(request, 'book_table.html')

def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('des', '').strip()
        rating = request.POST.get('rate', '').strip()
        image = request.FILES.get('image')  
        
        if name and description and rating:
            feedback = Feedback(User_name=name, Description=description, Ratting=rating, Image=image)
            feedback.save()
            
            return render(request, 'feedback.html', {'success': True})
    
    return render(request, 'feedback.html')


