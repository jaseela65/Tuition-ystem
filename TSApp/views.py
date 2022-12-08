import re
from urllib.request import Request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from TSApp.models import Atndns,TSclass,TSsubject,TSstudent,TSteacher,fee,lv,axept,rjt,results,task,ctask
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.contrib import messages
from multiprocessing import context
import random
from django.conf import settings
from django.core.mail import send_mail
import datetime
#import random
# Create your views here.
def homes(request):
    return render(request,'home.html/#signup')


def  home(request):

    #https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
    characters = list('abcdefghijklmnopqr0123456789stuvwxyzABCDEFGHIJKL!@#$%^&*()?><:;MNOPQRSTUVWXYZ')
    thepassword = ''
    for x in range(8):
        thepassword += random.choice(characters)



    css = list('1234567890')
    sid= "S"
    length=4

    for x in range(1,5):
        sid = sid + random.choice(css)

    cls=TSclass.objects.all()
    return render(request,'home.html',{'cls':cls,'sid':sid, 'thepassword':thepassword})

   
def adminhome(request):
    return render(request,'adminhome.html')
@login_required(login_url='SLogin')
def userhome(request):
    s=TSstudent.objects.get(user=request.user)
    return render(request,'userhome.html',{'s':s})
@login_required(login_url='SLogin')
def tcrhome(request):
    t=TSteacher.objects.get(user=request.user)
    return render(request,'thome.html',{'t':t})
def passwords():
    
    #length = int(request.GET.get('length'))
    #length = int([length])
    characters = list('abcdefghijkABCDEFGHIJKLMNOPQRSTUVWXYZlmnopqrstuvwxyz')
    #if request.GET.get('uppercase'):
       # characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
 
    #if request.GET.get('special'):
#characters.extend(list('£$%^&*!{}()'))
     
    #if request.GET.get('numbers'):
      #  characters.extend(list('0123456789'))

    password = ""
    length=4
 
#3i=0
   # while i < length:
   #     i=i+1
    for x in range(1,5):
        password = password + random.choice(characters)
    #return render(request, 'signup.html', {'password': thepass})
    return password

def passwordsm(request):
    
   
    characters = list('abcdefghijkABCDEFGHIJKLMNOPQRSTUVWXYZlmnopqr1234567890stuvwxyz£$%^&*!{}()wxyz')
   

    thepass = ""
    length=8

    for x in range(1,9):
        thepass = thepass + random.choice(characters)
    return render(request, 'signup.html', {'password': thepass})

def passwordss(request):
    
   
    characters = list('abcdefghijkABCDEFGHIJKLMNOPQRSTUVWXYZlmnopqr1234567890stuv£$%^&*!{}()wxyz')
   

    thepass = ""
    length=8

    for x in range(1,9):
        thepass = thepass + random.choice(characters)
    return render(request, 'signup.html', {'password': thepass})




def signup_page(request):
    #https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
  
    
    characters = list('abcdefghijklmnopqr0123456789stuvwxyzABCDEFGHIJKL!@#$%^&*()?><:;MNOPQRSTUVWXYZ')
    thepassword = ''
    for x in range(8):
        thepassword += random.choice(characters)

    #return render(request, 'generator/password.html', {"password":thepassword})
  

    css = list('1234567890')
   

    sid= "S"
    length=4

    for x in range(1,5):
        sid = sid + random.choice(css)

    cls=TSclass.objects.all()
    return render(request,'signup.html',{'cls':cls,'sid':sid, 'thepassword':thepassword})
def tlogin(request):
    return render(request,'login.html')




def usercreate(request):
    if request.method=='POST':
        sid=request.POST['sid']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        gender=request.POST['gender']
        age=request.POST['age']
        fkey=request.POST['classes']#course
        classes= TSclass.objects.get(id=fkey)
        #subjects=request.POST['subjects']
        mobile=request.POST['mobile']
        email=request.POST['email']
        image=request.FILES.get('image')
        username=request.POST['username']
        password=request.POST['password']
        #password=random.randint(10000,99999)
        cpassword=request.POST['cpassword']
        


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This Username already Exists')
                return redirect('usercreate')

                
            #elif User.objects.filter(email=email).exists():
               ## messages.info(request,'Email not available..')
               # print('Email not Available')
                #return redirect('signup_page')

                
            else:
                user=User.objects.create_user(
                    first_name= firstname,
                    last_name= lastname,
                    username= username,
                    password= password,email=email
                )
                user.save()
                u=User.objects.get(id= user.id)
                stu=TSstudent(sid=sid,address=address,
                gender=gender,
                age=age,
                classes=classes,
                mobile=mobile,image=image,user=u)
                sc_group = Group.objects.get(name = 'Tsstudent')
                sc_group.user_set.add(user)
                stu.save()
                messages.success(request,'successfully registered')
                subject='Tuition Management System'

                message='Dear user, You are Successfully Registered.\n Your Password is : ' f'{password}'
                recipient=request.POST['email']
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
                return redirect('home')
        else:

           messages.info(request,'Password Does not Match!!!!') 
           print('Password is not Matching')        
           return redirect('home')   
        #return redirect('home') 
    classes=TSclass.objects.all()
    context={
        'cLasses':classes
    }
    return render(request,'home.html',context)

def SLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('adminhome')#adminhome
            else:

                if user.groups.filter(name='Tsteacher').exists():
                    auth.login(request,user)
                    messages.info(request, f'Welcome {username}') 
                    return redirect('tcrhome')
                else:
                    auth.login(request,user)
                    messages.info(request, f'Welcome {username}') 
                    return redirect('userhome')#index        
        else:
            return redirect('SLogin')
    else:
        return redirect('home')#admin home

@login_required(login_url='SLogin')
def SLogout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')

def cls(request):
    return render(request,'addclass.html')
def addcls(request):
    if request.method== 'POST':
        classes=request.POST['classes']
        syllabus=request.POST['syllabus']
        clas=TSclass(classes=classes,syllabus=syllabus)
        clas.save()
        return redirect('cls')

def sbjt(request):
    return render(request,'addsubjt.html')
def addsbjt(request):
    if request.method== 'POST':
        subject=request.POST['subject']
        sbt=TSsubject(subject=subject)
        sbt.save()
        return redirect('sbjt')

def tcr(request):
    characters = list('abcdefghijklmnopqr0123456789stuvwxyzABCDEFGHIJKL!@#$%^&*()?><:;MNOPQRSTUVWXYZ')
    thepassword = ''
    for x in range(6):
        thepassword += random.choice(characters)


    sb=TSsubject.objects.all()
    return render(request,'addteacher.html',{'sb':sb,'thepassword':thepassword})
def addtcr(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        gender=request.POST['gender']
        age=request.POST['age']
        select=request.POST['subject']
        subject=TSsubject.objects.get(id=select)
        mobile=request.POST['mobile']
        email=request.POST['email']
        image=request.FILES.get('image')
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('tcr')
            else:
                user=User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                u = User.objects.get(id = user.id)

                tcr=TSteacher(address=address,gender=gender,age=age,subject=subject,
                mobile=mobile,image=image,user=u)
                tc_group = Group.objects.get(name = 'Tsteacher')
                tc_group.user_set.add(user)
                tcr.save()
                #messages.success(request,'successfully registered')
                subject='Tuition Management System'

                message='Dear user, You are Successfully Joined In Tuition Management System.\n Your Password is : ' f'{password}'
                recipient=request.POST['email']
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
                return redirect('tcr')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('adminhome')

       
    return render(request,'addteacher.html')


def showstd(request):
    if not request.user.is_staff:
        return redirect('usercreate')
    std=TSstudent.objects.all()
    return render(request,'showstudent.html',{'std':std})

def delstd(request,id):
    if not request.user.is_staff:
        return redirect('usercreate')
    suser=TSstudent.objects.get(id=id)
    suser.delete()
    return redirect('showstd')


def showtcr(request):
    tcr=TSteacher.objects.all()
    return render(request,'ashowteacher.html',{'tcr':tcr})

def ushowtcr(request):
    tcr=TSteacher.objects.all()
    t=TSstudent.objects.get(user_id=request.user)
    return render(request,'ushowteachers.html',{'tcr':tcr,'t':t})



def deltcr(request,id):
    if not request.user.is_staff:
        return redirect('usercreate')
    suser=TSteacher.objects.get(id=id)
    suser.delete()
    return redirect('showtcr')

def ttdProfile(request):
    t=TSteacher.objects.get(user_id=request.user)
    return render (request,'tshowprofile.html',{'t':t})


def stdProfile(request):
    s=TSstudent.objects.get(user_id=request.user)
    return render (request,'uprofile.html',{'s':s})

def timetable(request):
    s=TSclass.objects.all()
    return render(request,'addTimetable.html',{'s':s})

def ats(request):
    atns=TSstudent.objects.all()
    u=User.objects.filter(groups__name='Tsstudent')
    return render(request,'addAttendance.html',{'atns':atns,'u':u})
def add_atns(request):
    if request.method== 'POST':
        #ids=request.POST['sid']
        
        usi=request.POST['username']
        username=User.objects.get(id=usi)
        sid=TSstudent.objects.get(user=username)
        date=request.POST['date']
        atndns=request.POST['atndns']

        ns=Atndns(sid=sid,username=username,date=date,atndns=atndns)
        ns.save()
        st=TSstudent.objects.all()
        user=User.objects.all()
        return render(request,'addAttendance.html',{'st':st,'user':user})

@login_required(login_url='SLogin')
def view_atnss(request):
    if request.method=='POST':
        sdate=request.POST['sdate']
        tdate=request.POST['tdate']
        t=TSstudent.objects.get(user_id=request.user)
        an=Atndns.objects.filter(username=request.user,date__gt=sdate,date__lt=tdate)
        return render (request,'viewAtnstt.html',{'an':an,'t':t})
       
@login_required(login_url='SLogin')
def view_atns(request):
    t=TSstudent.objects.get(user_id=request.user)
    an=Atndns.objects.filter(username=request.user)
    return render (request,'viewAtns.html',{'an':an,'t':t})

def pyd(request):
    atns=TSstudent.objects.all()
    u=User.objects.filter(groups__name='Tsstudent')
    return render(request,'addfee.html',{'atns':atns,'u':u})
def add_fee(request):
    if request.method== 'POST':
        #ids=request.POST['sid']
        #sid=TSstudent.objects.get(id=ids)
        usi=request.POST['username']
        username=User.objects.get(id=usi)
        sid=TSstudent.objects.get(user=username)
       # b=TSstudent.objects.filter(sid_id=sid_id).order_by('user')
        date=request.POST['date']
        amount=request.POST['amount']
        paid=request.POST['paid']

        ns=fee(sid=sid,username=username,date=date,amount=amount,paid=paid)
        ns.save()
        st=TSstudent.objects.all()
        user=User.objects.all()
        return render(request,'addfee.html',{'st':st,'user':user})

def tsk(request):
    t=TSteacher.objects.get(user_id=request.user)
    u=User.objects.filter(groups__name='Tsstudent')
                   
    v=TSstudent.objects.all()
    
    return render(request,'taddtask.html',{'t':t,'u':u,'v':v})
def add_tsk(request):
    if request.method== 'POST':
       
        usi=request.POST['username']
        username=User.objects.get(id=usi)
        sid=TSstudent.objects.get(user=username)
        subject=request.POST['subject']
        taske=request.POST['taske']
        s_date=request.POST['s_date']
        e_date=request.POST['e_date']
        

        ns=task(sid=sid,username=username,subject=subject,
        taske=taske,s_date=s_date,e_date=e_date)
        ns.save()
        st=TSteacher.objects.all()
        user=User.objects.all()
        return redirect('tsk')
@login_required(login_url='SLogin')
def show_updtsk(request):
    t=TSteacher.objects.get(user_id=request.user)
    u=User.objects.filter(groups__name='Tsstudent')
                   
    v=TSstudent.objects.all()
    #z=TSteacher.objects.filter(subject=)
    w=ctask.objects.filter(subject=t.subject)
    return render(request,'tverftask.html',{'t':t,'u':u,'v':v,'w':w})

def vupdate_page(request,id):
    st = ctask.objects.get(pk = id)
    t=TSteacher.objects.get(user_id=request.user)
    return render (request,'tverftaskA.html',{'st':st,'t':t})

@login_required(login_url='SLogin')
def vupdate_tsk(request,id):
    if request.method=="POST":
        st=ctask.objects.get(pk = id)
        t=TSteacher.objects.get(user_id=request.user)
        #=request.POST.get('sid')
        #st.sid=request.POST.get('username')
        st.subject=request.POST.get('subject')
        st.taske=request.POST.get('taske')
        st.s_date=request.POST.get('s_date')
        st.e_date=request.POST.get('e_date')
        #st.attachment=request.FILES.get('attachment')
        st.pgrs=request.POST['pgrs']
        #st.pgrs.save()
        st.save()
        t.save()
        return redirect('show_updtsk')
   

      
@login_required(login_url='SLogin')
def show_ctsk(request):
    t=TSstudent.objects.get(user_id=request.user)
    an=ctask.objects.filter(username=request.user,pgrs='100')
    return render (request,'ucompltdtasks.html',{'an':an,'t':t})

@login_required(login_url='SLogin')
def show_tsk(request):
    t=TSstudent.objects.get(user_id=request.user)
    an=task.objects.filter(username=request.user, ctask__isnull=True)
    return render (request,'ushowtask.html',{'an':an,'t':t})

def update_page(request,id):
    st = task.objects.get(pk = id)
    t=TSstudent.objects.get(user_id=request.user)
    return render (request,'uupdatetask.html',{'st':st,'t':t})

@login_required(login_url='SLogin')
def update_tsk(request,id):
    if request.method=="POST":
        st=task.objects.get(pk = id)
        #t=TSstudent.objects.get(user_id=request.user)
        #st.sid.sid=request.POST.get('sid')
        #st.sid=request.POST.get('username')
        st.subject=request.POST.get('subject')
        st.taske=request.POST.get('taske')
        st.s_date=request.POST.get('s_date')
        st.e_date=request.POST.get('e_date')
        attachment=request.FILES.get('attachment')
        pgrs=request.POST['pgrs']
       # sid=st.sid.sid
        stu=ctask.objects.create(sid=st,username=request.user,subject=st.subject,
        taske=st.taske,s_date=st.s_date,e_date=st.e_date,
        attachment=attachment,pgrs=pgrs)
        stu.save()
        #st.delete()
        #t.save()
        return redirect('show_tsk')
   

      
@login_required(login_url='SLogin')
def show_fee(request):
    t=TSstudent.objects.get(user_id=request.user)
    an=fee.objects.filter(username=request.user)
    return render (request,'showfee.html',{'an':an,'t':t})

def tedit_page(request):
    stdt=TSteacher.objects.get(user_id=request.user)
    return render(request,'teditPrf.html',{'std':stdt})
    
      
@login_required(login_url='SLogin')
def tedit_std_details(request):
    if request.method=="POST":
        stdt=TSteacher.objects.get(user_id=request.user)
        st=User.objects.get(id=request.user.id)
        st.username=request.POST.get('username')
        stdt.address=request.POST.get('address')
        stdt.gender=request.POST.get('gender')
        stdt.age=request.POST.get('age')
        stdt.subject=request.POST.get('subject')

        stdt.mobile=request.POST.get('mobile')
        st.email=request.POST.get('email')
        st.save()
        stdt.save()
        return redirect('ttdProfile')
def edit_page(request):
    stdt=TSstudent.objects.get(user_id=request.user)
    return render(request,'editPrf.html',{'std':stdt})
    
      
@login_required(login_url='SLogin')
def edit_std_details(request):
    if request.method=="POST":
        stdt=TSstudent.objects.get(user_id=request.user)
        st=User.objects.get(id=request.user.id)
        st.username=request.POST.get('username')
        stdt.address=request.POST.get('address')
        stdt.gender=request.POST.get('gender')
        stdt.age=request.POST.get('age')
        stdt.subjects=request.POST.get('subjects')
        stdt.mobile=request.POST.get('mobile')
        st.email=request.POST.get('email')
        st.save()
        stdt.save()
        return redirect('stdProfile')

def leaves(request):
    stdt=TSstudent.objects.get(user_id=request.user)
    return render(request,'userLeave.html',{'std':stdt})

def add_leave(request):
    if request.method=='POST':
        sids=TSstudent.objects.get(user_id=request.user)
        usernm=User.objects.get(id=request.user.id)
        sid=request.POST['sid']
        username=request.POST['username']
        f_date=request.POST['f_date']
        T_date=request.POST['T_date']
        reason=request.POST['reason']
        sid=sids
        username=usernm
        ns=lv(sid=sid,username=username,f_date=f_date,T_date=T_date,reason=reason)
        ns.save()
        return redirect('leaves')

def showleaves(request):
    aps=lv.objects.all()
    return render(request,'acptlv.html',{'aps':aps})

def approve(request,id):
    sids=lv.objects.get(id=id)
    dt=axept.objects.create(sid=sids,user=request.user)
    dt.save()
    #sids.delete()
    return redirect('showleaves')

def rjts(request,id):
    sids=lv.objects.get(id=id)
    dt=rjt.objects.create(sid=sids,user=request.user)
    dt.save()
    #sids.delete()
    return redirect('showleaves')


    #sids=axept.objects.filter(user_id=request.user.id)
    #sids=axept.objects.filter(user=request.username)
    #sids=axept.objects.filter(username_id=request.user.id)
    #sr=rjt.objects.all()
    #sa=axept.objects.get(user_id=request.user.id)
    #sr=rjt.objects.filter(id=request.user.id)
   
    #sr=rjt.objects.filter(user=request.user.username)
    #return render(request,'uviewStatus.html',{'t':t,'sids':sids })

def load_usn(request):
    sid_id=request.GET.get('sid')
    b=TSstudent.objects.filter(sid_id=sid_id).order_by('user')
    return render(request,'addResult.html',{'b':b})

def rslt_page(request):
    s=TSstudent.objects.all()
    sid=request.GET.get('sid')
    #u=TSstudent.objects.filter(sid=sid).order_by('user')
    u=User.objects.filter(groups__name='Tsstudent')
    c=TSclass.objects.all()
    return render(request,'addResult.html',{'s':s,'u':u,'c':c})

def reslt(request):
     if request.method== 'POST':
      
        #sid=TSstudent.objects.get(id=ids)
        usi=request.POST['username']
        username=User.objects.get(id=usi)
        sid=TSstudent.objects.get(user=username)
        #usi=request.POST.get("sid")
        #username=TSstudent.filter(sid=usi).first()

        cls=request.POST['classes']#course
        classes=TSclass.objects.get(id=cls)
        exam=request.POST['exam']
        mal=request.POST['mal']
        hid=request.POST['hid']
        es=request.POST['es']
        ms=request.POST['ms']
        ps=request.POST['ps']
        cmy=request.POST['cmy']
        bgy=request.POST['bgy']
        ss=request.POST['ss']
        inft=request.POST['inft']
        
        ns=results(sid=sid,username=username,classes=classes,exam=exam,mal=mal,hid=hid,es=es,ms=ms,ps=ps,cmy=cmy,bgy=bgy,ss=ss,inft=inft)
        ns.save()
        st=TSstudent.objects.all()
        user=User.objects.all()
        cls=TSclass.objects.all()
        return render(request,'adminhome.html',{'st':st,'user':user,'cls':cls})
@login_required(login_url='SLogin')
def show_result(request):
    t=TSstudent.objects.get(user_id=request.user)
    an=results.objects.filter(username=request.user).order_by('-id')[:1]
    return render (request,'showResult.html',{'an':an,'t':t})


@login_required(login_url='SLogin')
def approve_appointment(request,pk):
    appointment1=lv.objects.get(id=pk)
    appointment1.status=1
    appointment1.save()
    #messages.success(request,'Your appointment request is approved')

    return redirect('showleaves')

@login_required(login_url='SLogin')
def reject_appointment(request,pk):
    appointment1=lv.objects.get(id=pk)
    appointment1.status = 2
    appointment1.save()
    #messages.error(request,'Your appointment request is rejected')
    return redirect('showleaves')

@login_required(login_url='SLogin')
def showlst(request):
    t=TSstudent.objects.get(user_id=request.user)
    #lvar=lv.objects.all()
    lvar=lv.objects.filter(sid_id=t.id,status=1)
    lvaa=lv.objects.filter(sid_id=t.id,status=2)
    
    return render(request,'uviewStatus.html',{'lvar':lvar,'t':t,'lvaa':lvaa})


def del_lvs(request,id):
    if not request.user.is_staff:
        return redirect('usercreate')
    suser=lv.objects.get(id=id)
    suser.delete()
    return redirect('showleaves')

#https://stackoverflow.com/questions/68037403/filter-data-between-two-dates-django