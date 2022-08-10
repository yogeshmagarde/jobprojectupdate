from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Registration
from . models import candidate
from . models import HrReg
from . models import Job1
from . models import Resume


def login(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session["sessemail"]=request.POST["email"]
            if request.POST.get("chk"):
                res = HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location']='resume'
                return res
        else:
                return render(request,"jobapp/Login.html",{"msg":"invalid userid and password"})
    else:
        c1=''
        c2=''
    if request.COOKIES.get('ukey'):
        c1=request.COOKIES['ukey']
        c2=request.COOKIES['upass']
    return render(request,"jobapp/Login.html",{'ucookie':c1,'pcookie':c2})

def registration(request):
    Qulification=["10th","12th","diploma","graduation","post graduation"]
    if request.method=="POST":
        r=Registration(email=request.POST["email"],password=request.POST["password"],
        mobile=request.POST["mobile"],technology=request.POST["technology"],
        candidatetype=request.POST["type"],higereducation=request.POST["education"],
        Passingyear=request.POST["applydate"])
        r.save()
        return render(request,"jobapp/Login.html",{"data":Qulification,"data":"registration sucsessfully"})
    return render(request,"jobapp/Registrationform.html",{"data":Qulification})

def job(request):
    if(request.session.has_key('sessemail')):
        suid=request.session['sessemail']
        data1 = Job1.objects.all()
        return render(request,"jobapp/job.html",{"d":"data inser sucsessfully","res":Job1.objects.all()})
    else:
        return redirect('login')

def Candidate(request):
    if(request.session.has_key('sessemail')):
        suid=request.session['sessemail']
        data1 = Job1.objects.all()
        ds1 = candidate.objects.all()
        if request.method=="POST":
            c = candidate(emailid=request.POST["txtemail"],jobid=request.POST["ddljob"],applydate=request.POST["applydate"],cname=request.POST["cname"])
            c.save()
            return render(request,"jobapp/cds.html",{"res1":data1,"msg":"Apply sucsessfully","ds":ds1})
        return render(request,"jobapp/Candidate.html",{"res1":data1,"jid":(request.GET["q"]),"ds":ds1})
    else:
        return redirect('login')

def cds(request):
    return render(request,"jobapp/cds.html",{"ds":candidate.objects.all()})

def hrreg(request):
    if request.method=="POST":
        r = HrReg(emailid=request.POST["emailid"],password=request.POST["password"],
            mobile=request.POST["mobile"],companyname=request.POST["company"])
        r.save()
        return render(request,"jobapp/hrlogin.html")
    return render(request,"jobapp/hrreg.html")
def insertjob(request):
    if request.method=="POST":
        r = Job1(jobtitle=request.POST["txtt"],jobdiscription=request.POST["txtd"],
            experience=request.POST["txte"],technology=request.POST["txtte"],
            postdate=request.POST["txtp"],duedate=request.POST["txtdu"])
        r.save()
        return render(request,"jobapp/job.html",{"res":Job1.objects.all()})
    return render(request,"jobapp/insertjob.html",{"res":Job1.objects.all()})

def hrlogin(request):
    if request.method=="POST":
        r = HrReg.objects.filter(emailid=request.POST["emailid"],password=request.POST["password"])
        if r.count()>0:
            request.session["sessemail"]=request.POST["emailid"]
            if request.POST.get("chk"):
                res = HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["emailid"])
                res.set_cookie('upass',request.POST["password"])
                res['Location']='insertjob'
                return res
        else:
                return render(request,"jobapp/hrlogin.html",{"msg":"invalid userid and password"})
    else:
        c3=''
        c4=''
    if request.COOKIES.get('ukey'):
        c3=request.COOKIES['ukey']
        c4=request.COOKIES['upass']
    return render(request,"jobapp/hrlogin.html",{'ucookie':c3,'pcookie':c4})

def Logout(request):
    res=HttpResponse(status=302)
    res.delete_cookie('ukey',"/")
    res.delete_cookie('upass',"/")
    del request.session["sessemail"]
    res['Location']='dash'
    return res

def dash(request): 
    return render(request,"jobapp/home.html")

def resume(request):
    if(request.session.has_key('sessemail')):
        suid=request.session['sessemail']
        data1 = Resume.objects.all()
        r1 = None
        data=['select state',' ','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat',
        'Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra',
        'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
        'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

        branch=['select',' ','General','Mathematics','Biology','Automobile Engineering','Computer Science','Electronics & Communication ','Electrical Engineering','Electronics & Communication ','Agricultural Engineering',
        'Architectural Engineering','Information Technology','Civil Engineering']

        year=['select',' ','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']

        course=['select',' ','10','12','DIPLOMA','Graduation','PostGraduation','Phd']

        if request.method=="POST":
            r1 = Resume(name=request.POST["txt1"],gender=request.POST["txt2"],locality=request.POST["txt3"],
                 city=request.POST["txt4"],pin=request.POST["txt5"],state=request.POST["txt6"],
                 mobile=request.POST["txt7"],email=request.POST["txt8"],job_city=request.POST["txt9"],
                 Address=request.POST["txt10"],linkedin=request.POST["txt11"],Objective=request.POST["txt12"],
                 Workexperience=request.POST["txt13"],ITSKILLS=request.POST["txt21"],PROJECTS=request.POST["txt15"],
                 TRAININGS=request.POST["txt16"],HOBBIESINTEREST=request.POST["txt17"],DECLARATION=request.POST["txt18"],
                 Date=request.POST["txt19"],sname=request.POST["txt20"],
                 course=request.POST["txt22"],branch=request.POST["txt23"],
                 Passingyear=request.POST["txt24"],percentage=request.POST["txt14"],univercity=request.POST["txt37"],
                 dcourse=request.POST["txt25"],dbranch=request.POST["txt26"],
                 dPassingyear=request.POST["txt27"],dpercentage=request.POST["txt28"],dunivercity=request.POST["txt38"],
                 gcourse=request.POST["txt29"],gbranch=request.POST["txt30"],
                 gPassingyear=request.POST["txt31"],gpercentage=request.POST["txt32"],gunivercity=request.POST["txt39"],
                 pgcourse=request.POST["txt33"],pgbranch=request.POST["txt34"],
                 pgPassingyear=request.POST["txt35"],pgpercentage=request.POST["txt36"],pgunivercity=request.POST["txt40"]) 
            r1.save()
            return render(request,"jobapp/show.html",{"y":year,"b":branch,"c":course,"res":data,"d":Resume.objects.filter(id=r1.id)})
        return render(request,"jobapp/resume.html",{"y":year,"b":branch,"c1":course,"res":data,"d":Resume.objects.all()})
    else:
        return redirect('login')
def show(request):
    return render(request,"jobapp/show.html",{"d":Resume.objects.all()})




    


# Create your views here.
