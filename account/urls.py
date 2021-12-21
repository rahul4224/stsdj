from django.contrib import admin
from django.urls import path
from account import views

admin.site.site_header = "Career Devlopment Cell Admin"
admin.site.site_title = "GMIT|CDC|ADMIN"
admin.site.index_title = "Gargi Memorial Institute Of Technology Career Devlopment Cell"

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout,name='signout'),
    path('forget/', views.forget, name='forget'),
    path('student/', views.student, name='student'),
    path('studentedit/', views.studentedit, name='studentedit'),
    path('activity/', views.activity, name='activity'),
    path('academic/', views.academic, name='academic'),
    path('Professor/', views.Professor, name='Professor'),
    
    path('allstudent/', views.allstudent, name='allstudent'),
    path('addacademic/<int:pk>', views.addacademic, name='addacademic'),
    path('viewacademic', views.viewacademic, name='viewacademic'),


]
