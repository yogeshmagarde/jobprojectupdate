from django.db import models


class Registration(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    technology = models.CharField(max_length=50)
    candidatetype = models.CharField(max_length=50)
    higereducation = models.CharField(max_length=50)
    Passingyear = models.CharField(max_length=50, default=' ')



class candidate(models.Model):
    emailid = models.CharField(max_length=50)
    jobid = models.CharField(max_length=50)
    applydate = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)

class HrReg(models.Model):
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50)
    
class Job1(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdiscription = models.CharField(max_length=500)
    experience = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    postdate = models.CharField(max_length=100)
    duedate = models.CharField(max_length=100)
    


class Resume(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    job_city = models.CharField(max_length=50)
    Address = models.CharField(max_length=50, default=' ')
    linkedin = models.CharField(max_length=50, default=' ')
    Objective = models.CharField(max_length=50, default=' ')
    Workexperience = models.CharField(max_length=500, default=' ')
    ITSKILLS = models.CharField(max_length=500, default=' ')
    PROJECTS = models.CharField(max_length=500, default=' ')
    TRAININGS = models.CharField(max_length=500, default=' ')
    HOBBIESINTEREST = models.CharField(max_length=500, default=' ')
    DECLARATION = models.CharField(max_length=500, default=' ')
    Date = models.CharField(max_length=50, default=' ')
    sname = models.CharField(max_length=50, default=' ')
    percentage = models.CharField(max_length=500, default=' ')
    branch = models.CharField(max_length=50, default=' ')
    Passingyear = models.CharField(max_length=50, default=' ')
    course = models.CharField(max_length=50, default=' ')
    univercity = models.CharField(max_length=50, default=' ')


    dpercentage = models.CharField(max_length=500, default=' ')
    dbranch = models.CharField(max_length=50, default=' ')
    dPassingyear = models.CharField(max_length=50, default=' ')
    dcourse = models.CharField(max_length=50, default=' ')
    dunivercity = models.CharField(max_length=50, default=' ')


    gpercentage = models.CharField(max_length=500, default=' ')
    gbranch = models.CharField(max_length=50, default=' ')
    gPassingyear = models.CharField(max_length=50, default=' ')
    gcourse = models.CharField(max_length=50, default=' ')
    gunivercity = models.CharField(max_length=50, default=' ')


    pgpercentage = models.CharField(max_length=500, default=' ')
    pgbranch = models.CharField(max_length=50, default=' ')
    pgPassingyear = models.CharField(max_length=50, default=' ')
    pgcourse = models.CharField(max_length=50, default=' ')
    pgunivercity = models.CharField(max_length=50, default=' ')





    

# Create your models here.

# Create your models here.
