from django.urls import path
from. import views
urlpatterns=[
    path('registration',views.registration),
    path('login',views.login,name='login'),
    path('Logout',views.Logout,name='Logout'),
    path('job',views.job,name='job'),
    path('Candidate',views.Candidate,name='Candidate'),
    path('cds',views.cds,name='cds'),
    path('hrreg',views.hrreg,name='hrreg'),
    path('hrlogin',views.hrlogin,name='hrlogin'),
    path('insertjob',views.insertjob,name='insertjob'),
    path('resume',views.resume,name='resume'),
    path('dash',views.dash),
    path('show',views.show,name='show'),
   
   
]