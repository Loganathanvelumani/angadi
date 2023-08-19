from django.shortcuts import render
from .models import work
from .models import Register
from .models import complete
# Create your views here.


def task(request):
    if request.method=='POST':
        TITTEL=request.POST['s_tit']
        DES=request.POST['s_dec']
        obj=work()
        obj.Tittel=TITTEL
        obj.Description=DES
        obj.save()
        mydata=work.objects.all()
        one=complete.objects.all()
        return render (request,'main.html',{'value0':mydata,'value2':one})
    return render(request,'task_form.html')

def update(request,id):
    givdata=work.objects.get(id=id)
    mydata=work.objects.all()
    if request.method=='POST':
        TITTEL=request.POST['s_tit']
        COM=request.POST.get('check',None)
        
        if COM == 'Done':
            for i in mydata:
                if i.id==givdata.id:
                    global one
                    obj=complete()
                    obj.Done=givdata.Tittel
                    obj.save()
                    one=complete.objects.all()
                    givdata.delete()
                elif i.id!=givdata.id:
                    global out1
                    out1=work.objects.all()
            return  render(request,'main.html',{'value2':one,'value0':out1})
    
    return render (request,'task_form.html',{'value1':givdata})




def delete(request,id):
    givdata=work.objects.get(id=id)
    givdata.delete()
    mydata=work.objects.all()
    if  givdata.id not in mydata:
        return render(request,'main.html',{'value':mydata})
    return render (request,'main.html')


def register(request):
    if request.method=='POST':
        NAME=request.POST['s_name']
        PASSWORD=request.POST['s_pass']
        CONPASS=request.POST['s_com']
        obj=Register()
        obj.Name=NAME
        obj.Password=PASSWORD
        obj.Conpass=CONPASS
        obj.save()
        return render(request,'index.html')
    return render(request,'register.html')

def login(request):
    mydata=Register.objects.all()
    if request.method=='POST':
        NAME=request.POST['s_name']
        PASSWORD=request.POST['s_pass']
        out3=1
        for i in mydata:
            if i.id == out3:
                name=i.Name
                p_word=i.Password
                c_pass=i.Conpass
                if name==NAME and p_word == PASSWORD:
                    out=i.Name
                    mydata=work.objects.all()
                    return render(request,'main.html',{'key':out})
                elif name!=NAME and p_word ==PASSWORD:
                    out1='Username is Wrong'
                    return render(request,'index.html',{'key1':out1})
                elif name==NAME and p_word !=   PASSWORD:
                    out2='Password is wrong'
                    return render(request,'index.html',{'key2':out2})
                elif name!=NAME and p_word !=  PASSWORD:
                        out3+=1         
    return  render(request,'index.html')

def comdelete(request,id):
    givdata=complete.objects.get(id=id)
    givdata.delete()
    mydata=complete.objects.all()
    out1=work.objects.all()
    if  givdata.id not in mydata:
        return render(request,'main.html',{'value2':mydata,'value0':out1})
    return render (request,'main.html')

