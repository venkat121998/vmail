from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import vmailuser,Vmails
from .forms import CreateForm,LoginForm,ComposeForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'vmail/index.html')

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            mail = request.POST['mail_id']
            try:
                mail_id = vmailuser.objects.get(mail_id=mail)
            except:
                mail_id = None
            if mail_id:
                return HttpResponse("user aldredy exist")
            else:
                post = form.save(commit=False)
                post.created_at = datetime.now()
                post.save()
                id = post.id
                user = vmailuser.objects.get(id=id)
                user.login = 1
                user.save()
                l = user.login
                Z=1
                mail = {}
                return render(request,'vmail/user.html',{'users':user,'mails':mail,'z':Z,'message':'Your Account Has Been Succefully Created','l':l})
    else:
        form = CreateForm()
    return render(request, 'vmail/create.html', {'form': form})

def logins(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            vmail = request.POST['vmail']
            password = request.POST['password']
            try:
                user = vmailuser.objects.get(mail_id=vmail,password=password)#authenticate(request,mail_id=vmail, password=password)vmailuser.objects.get(mail_id=vmail)
            except vmailuser.DoesNotExist:
                user = None           
            if user is not None:
                login(request, user)
                k=1
                user.login = 1
                user.save()
                l = user.login
                mail_read = Vmails.objects.filter(to_id=user.id).filter(visit=1).order_by('-sent_at')
                mail_unread = Vmails.objects.filter(to_id=user.id).filter(visit=0).order_by('-sent_at')
                return render(request,'vmail/user.html',{'users':user,'mails_read':mail_read,'mails_unread':mail_unread,'k':k,'l':l})
                #return HttpResponse("Authenticated")
            else:
                return HttpResponse("Not Authenticated")
    else:
        form = LoginForm()
    return render(request,'vmail/login.html',{'form':form})    
        
def compose(request,id):
    if request.method == "POST":
        form = ComposeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            mail = request.POST['to']
            k = vmailuser.objects.get(mail_id=mail)
            post.to_id = k.id            
            post.from_id = id
            post.sent_at = datetime.now()
            post.save()
            user = vmailuser.objects.get(id=id)
            l = user.login
            mail_read = Vmails.objects.filter(to_id=id).filter(visit=1).order_by('-sent_at')
            mail_unread = Vmails.objects.filter(to_id=id).filter(visit=0).order_by('-sent_at')
            return render(request,'vmail/user.html',{'users':user,'mails_read':mail_read,'mails_unread':mail_unread,'l':l})
    else:
        form = ComposeForm()
        v = vmailuser.objects.get(id=id)
        l = v.login
    return render(request, 'vmail/compose.html', {'form': form,'id':id,'v':v,'l':l})


def user(request,id):
    user = vmailuser.objects.get(id=id)
    l = user.login
    mail_read = Vmails.objects.filter(to_id=id).filter(visit=1).order_by('-sent_at')
    mail_unread = Vmails.objects.filter(to_id=id).filter(visit=0).order_by('-sent_at')
    return render(request,'vmail/user.html',{'users':user,'mails_read':mail_read,'mails_unread':mail_unread,'l':l})
def logouts(request,id):
    user = vmailuser.objects.get(id=id)
    user.login = 0
    user.save()
    l = user.login
    logout(request)
    for key in request.session.keys():
        del request.session[key]
    request.session.flush()
    k=1
    return render(request,'vmail/index.html',{'message':k,'l':l})

def details(request,ide,id):
    user = vmailuser.objects.get(id=id)
    mail_detail = Vmails.objects.get(id=ide)
    mail_detail.visit = 1
    mail_detail.save()
    l = user.login
    froms_id = vmailuser.objects.get(id=mail_detail.from_id)
    fid = froms_id.id
    uid = user.id
    return render(request,'vmail/details.html',{'mail_detail':mail_detail,'fid':fid,'uid':uid,'users':user,'from':froms_id,'l':l})

def sent(request,id):
    mails = Vmails.objects.filter(from_id=id).order_by('-sent_at')
    from_id = vmailuser.objects.get(id=id)
    l = from_id.login
    #To_id = vmailuser.objects.get(id=mails.to_id)
    return render(request,'vmail/sent.html',{'mails':mails,'users':from_id,'l':l})

def details_sent(request,ide,id):    
    user = vmailuser.objects.get(id=id)
    mail_detail = Vmails.objects.get(id=ide)
    To_id = vmailuser.objects.get(id=mail_detail.to_id)
    l = user.login
    return render(request,'vmail/details_sent.html',{'mail_detail':mail_detail,'users':user,'to':To_id,'l':l})