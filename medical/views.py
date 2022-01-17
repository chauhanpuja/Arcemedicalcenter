from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from. models import Contact,Post,Departmentt,Team,Appointment,Carrier
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    department=Departmentt.objects.all()
    team=Team.objects.order_by('-slug')[0:7]
    post=Post.objects.order_by('-date')[0:3]
    post={
        'post':post,
        'department':department,
        'team':team
    }
    return render(request,'index.html',post)

def about(request):
    department=Departmentt.objects.all()
    team=Team.objects.all
    team={
        'team':team,
        'department':department,
    }
    return render(request,'about.html',team)


def contact(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    if request.method=='POST': 
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        address=request.POST.get('address','')

        print(name)

        contact=Contact(name=name,email=email,phone=phone,desc=desc,address=address)
       
        subject=name
        message=desc
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from ,['poojachauhan2102@gmail.com'])
            contact.save()
            messages.info(request,"Message Sent Successfully")
            return redirect('/')
             
        except Exception as e:
            return redirect('/contact')

    return render(request,'contact.html',team)

def appointment(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    if request.method=='POST': 
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        department=request.POST.get('department','')
        doctor_name=request.POST.get('doctor_name','')
        date=request.POST.get('date','')
        msg=request.POST.get('msg','')
        
        
        appointment=Appointment(name=name,email=email,phone=phone,department=department,doctor_name=doctor_name,date=date,msg=msg)
        
        subject=name
        message=msg
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from ,['poojachauhan2102@gmail.com'])
            appointment.save()
            messages.info(request,"Book Appointment Successfully")
            return redirect('/')
        
        except Exception as e:
            return redirect("appointment")
    return render(request,'appointment.html',team)



def doctor(request):
    department=Departmentt.objects.all()
    team=Team.objects.all
    team={
        'team':team,
        'department':department,
    }
    return render(request,'doctor.html',team)

def carrier(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    if request.method=='POST': 
        carrier=request.POST.get('carrier','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        gender=request.POST.get('gender','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        exp=request.POST.get('exp','')
        resume=request.POST.get('resume','')
        education=request.POST.get('education','')
        skill=request.POST.get('skill','')
        
        
        carrier=Carrier(carrier=carrier,name=name,email=email,gender=gender,phone=phone,address=address,exp=exp,resume=resume,education=education,skill=skill)
        carrier.save()
        messages.info(request,"Successfully Submiited")
        return redirect('/')
    return render(request,'carrier.html',team)


def doctor_details(request,slug):
    department=Departmentt.objects.all()
    
    
    team=Team.objects.filter(slug=slug)
    team={
        'team':team,
        'department':department,
    }
    return render(request,'doctor_detail.html',team)

def pricing(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    return render(request,'pricing.html',team)

def project_details(request):
    
    return render(request,'project_details.html')


def services(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    return render(request,'services.html',team)

def blog(request):
    department=Departmentt.objects.all()
    post=Post.objects.all
    post={
        'post':post,
        'department':department,
    }
    return render(request,'blog.html',post)

def post(request,slug):
    department=Departmentt.objects.all()
    allpost=Post.objects.all
    post=Post.objects.filter(slug=slug)
    post={
        'post':post,
        'allpost':allpost,
        'department':department,
    }
    
    return render(request,'post.html',post)

def department(request,slug):
    
    department=Departmentt.objects.filter(slug=slug)
    
    department={
        
        'department':department
    }
    return render(request,'department.html',department)

def search(request):
    department=Departmentt.objects.all()
    
   
    query=request.GET['query']
    post=Post.objects.filter(title__icontains=query)
    # post=Post.objects.filter(desc__icontains=query)
    # post=Post.objects.filter(name__icontains=query)
    
    
    # post=Post.objects.filter(date__icontains=query)

    post={
        'post':post,
        'department':department,
    }
    return render(request,'search.html',post)


def time_table(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    return render(request,'time_table.html',team)

def userlogin(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request,'Successfully logged In')
            return redirect("/")

        else:
            messages.error(request,'User not Signup')
            return redirect('login') 

        

    return render(request,'login.html',team)
    
    
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')



def registration(request):
    department=Departmentt.objects.all()
    
    team={
        
        'department':department,
    }
    if request.method=="POST":
        username=request.POST.get('username')
        
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        # if User.objects.filter(name=name).exists():
        #     messages.info(request,"name already taken")
        #     return redirect("signup")
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already taken")
            return redirect("registration")


        # if len(username)>10:
        #     messages.error(request,"Username must be under 10 character")
        #     return redirect("signup")

        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("registration")
        
        if pass1 != pass2:
            messages.error(request,"Password do not matched")
            return redirect("registration")

        
        myuser=User.objects.create_user(username,email,pass1)
        
        myuser.save()

        
        messages.success(request,"User Created")
        return redirect("/")
        
    else:

        
        return render(request,'registration.html',team)
    
    

