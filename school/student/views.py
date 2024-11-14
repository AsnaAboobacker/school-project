from django.shortcuts import render
from .forms import StudForm,SForm
from .models import stud
# Create your views here.


def show(request):
    return render(request,'home.html')

def register(request):
    title="Student Registration"
    form = StudForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        aadhar = form.cleaned_data['s_aadhar']
        clas = form.cleaned_data['s_class']
        division = form.cleaned_data['s_division']
        egrantid = form.cleaned_data['s_egrantid']
        category = form.cleaned_data['s_category']
        gender = form.cleaned_data['s_gender']
        adr=stud.objects.filter(s_aadhar=aadhar)
        if len(adr)>0:
            return render(request, 'ack.html', {"title": "Student Already Exists... "})
        else:
            p = stud(s_name=name,s_aadhar=aadhar,s_class=clas,s_division=division,s_egrantid=egrantid,s_category=category
                 ,s_gender=gender)
            p.save()
            return render(request,'ack.html', {"title":"Registered Successfully"})
    context={
    "title":title,
    "form":form,
    }
    return render(request,'register.html',context)

def existing(request):
    title="All registered Students"
    queryset = stud.objects.all()

    context={
    "title":title,
    "queryset":queryset,
    }
    return render(request,'existing.html',context)

def search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request, 'ack.html',{'title':'Student Details Not Found.. Please Enter Correct Data'})
        context = {
            "title": title,
            'queryset': queryset,
        }
        return render(request,'existing.html',context)

    context={
        "title":title,
        'form':form,
    }
    return render(request,'search.html',context)

def dropout(request):
    title="Drop Out "
    form=SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset = stud.objects.filter(s_name=name)
        if len(queryset) == 0:
            return render(request, 'ack.html', {'title': 'Student Details Not Found.. Please Enter Correct Data'})
        else:
            queryset=stud.objects.filter(s_name=name).delete()
            return render(request,'ack.html',{'title':"Student removed from your Database"})

    context={
        "title":title,
        'form':form,
    }
    return render(request,'drop.html',context)