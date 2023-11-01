from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import StudentCreateForm,RegistrationForm,LoginForm
from crm.models import Students
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
# Create your views here.


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # form.save() user.object.create(**form.cleaned_data)
            print("saved")
            return redirect("login")
        else:
            return render(request,"registration.html",{"form":form})

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("stud-list")
            
            else:
                return render(request,"login.html",{"form":form})
        


        
            

        

class StudentCreateView(View):
    def get(self,request,*args,**kwargs):
        form=StudentCreateForm()
        return render(request,"student_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=StudentCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("stud-list")
        else:
            return render(request,"student_add.html",{"form":form})
        

class StudentListView(View):
    def get(self,request,*args,**kwargs):
        qs=Students.objects.all()
        return render(request,"student_list.html",{"students":qs})


class  StudentDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Students.objects.get(id=id)
        return render(request,"student_detail.html",{"student":qs})


class StudentUpdtaeView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        form=StudentCreateForm(instance=obj)
        return render(request,"student_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Students.objects.get(id=id)
        form=StudentCreateForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("stud-list")
        else:
            return render(request,"student_edit.html",{"form":form})
        

class StudentDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Students.objects.filter(id=id).delete()
        return redirect("stud-list")
        

