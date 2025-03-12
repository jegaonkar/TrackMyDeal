from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

def indexPage(request):
    sample_deals = [
        {"name": "iPhone 14", "price": "$799", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Samsung Galaxy S23", "price": "$699", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Sony Headphones", "price": "$199", "image_url": "https://via.placeholder.com/150", "link": "#"},
    ]
    return render(request, 'index.html', {'sample_deals': sample_deals})
    
def popularDeals(request):
    sample_deals = [
        {"name": "iPhone 14", "price": "$799", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Samsung Galaxy S23", "price": "$699", "image_url": "https://via.placeholder.com/150", "link": "#"},
        {"name": "Sony Headphones", "price": "$199", "image_url": "https://via.placeholder.com/150", "link": "#"},
    ]
    return render(request, 'CustomerPages/populardeals.html', {'sample_deals': sample_deals})

def logoutView(request):
    logout(request)
    return redirect('IndexPage') 

#customerLOgin page
def loginPage(request):
    return render(request, './AuthenticateCustomer/Login.html')

#validate customer login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('CustomerHomepage')
        else:
            messages.warning(request, 'Wrong login credentials')
            return redirect('LoginPage')
        
    return redirect('IndexPage')


#customer register page
def registerPage(request):
    return render(request, './AuthenticateCustomer/Register.html')

#validate customer register
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstName')
        last_name=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        #check wheather username is already taken or not 
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exist')
            return redirect('RegisterPage')

        #check wheather email is already taken or not 
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exist')
            return redirect('RegisterPage')
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        Customer.objects.create(user=user, address='', phone='')#creating customer with empty data to avoid customer does nt exist error while opening Account page for first time

        return redirect('LoginPage')
        
    return redirect('IndexPage')

@login_required
#customer homepage
def homePage(request):
    return render(request, './CustomerPages/Home.html')

@login_required
#customer Account page
def accountPage(request):
    user = request.user  # Logged-in user
    customer = Customer.objects.get(user=user)  # Associated customer data
    return render(request, './CustomerPages/Account.html', {'customerData':customer})

@login_required
def updateAccount(request):
    user = request.user  # Logged-in user
    customer = Customer.objects.get(user=user)  # Associated customer data

    if request.method == 'POST':
        # Get form data
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Update User model fields
        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        user.save()

        # Update Customer model fields
        customer.address = address
        customer.phone = phone
        customer.save()

        messages.success(request, 'Account updated successfully!')
        return redirect('CustomerAccountPage')

    return redirect('IndexPage')

@login_required
def changePassword(request):
    if request.method == 'POST':
        user = request.user
        currentPassword = request.POST['currentPassword']
        newPassword = request.POST['newPassword']
        
        if not user.check_password(currentPassword): #check password of current user
            messages.warning(request, "Wrong Password")

        else:
            user.set_password(newPassword)
            user.save()
            update_session_auth_hash(request, user)  #to keep the user logged in after password change
            messages.success(request, "Password updated successfully!")
        return redirect('CustomerAccountPage')
    return redirect('IndexPage')

@login_required
#customer service page
def servicePage(request):
    user = request.user
    
    full_name = user.get_full_name()
    email = user.email
    
    return render(request, './CustomerPages/Service.html', {
        'full_name': full_name,
        'email': email
    })
    
@login_required
def serviceSubmit(request):
    if request.method == "POST":
        requestType = request.POST.get('requestType')
        details = request.POST.get('details')
        fileAttachment = request.FILES.get('fileAttachment')

        # Get the logged-in customer's data
        customer = User.objects.get(username=request.user)

        service_request = ServiceRequest.objects.create(
            customer=customer,
            request_type=requestType,
            details=details,
            file_attachment=fileAttachment,
        )

        return redirect('TrackService')  

    return redirect('IndexPage')

@login_required
#customer service track page
def trackService(request):
    if request.user.is_authenticated:
        # Get the user's customer instance
        customer = request.user
        # Filter service requests for the logged-in user
        service_requests = ServiceRequest.objects.filter(customer=customer)
        return render(request, './CustomerPages/TrackService.html', {'service_requests': service_requests})
    else:
        return redirect('IndexPage')

    
    
    
    
    