from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('appointment',views.appointment,name="appointment"),
   
    path('doctor',views.doctor,name="doctor"),
    path('blog',views.blog,name="blog"),
    path('search',views.search,name='search'),
    path('post/<str:slug>',views.post,name="post"),
    path('department/<str:slug>',views.department,name="department"),
    path('doctor_details/<str:slug>',views.doctor_details,name="doctor_details"),

    path('login',views.userlogin,name="login"),
    path('job',views.job,name="job"),
    path('carrier',views.carrier,name="carrier"),
    
    path('handlelogout',views.handlelogout,name="handlelogout"),
    path('registration',views.registration,name="registration"),
    path('pricing',views.pricing,name="pricing"),
    path('project_details',views.project_details,name="project_details"),
    path('services',views.services,name="services"),
    path('time_table',views.time_table,name="time_table"),


    
]