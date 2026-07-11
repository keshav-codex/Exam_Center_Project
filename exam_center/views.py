from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExamCenterForm
from .models import ExamCenter

def add_exam_center(request):
    
    # for form submitting case
    if request.method == "POST":

        # collecting data
        form = ExamCenterForm(request.POST)

        #checking data -> save it -> redirect to view_exam_center url
        if form.is_valid():
            form.save()
            return redirect ("view_exam_center")

    # for first time -> create empty form  
    else:
        form = ExamCenterForm()

    # create context (dictionary in django terminology)
    context ={ "form":form }

    return render(request,"exam_center/add_exam_center.html",context)


def view_exam_center(request):

    # get details of all Exam Center
    exam_centers = ExamCenter.objects.all()
    context = { "exam_centers" : exam_centers }

    return render(request, "exam_center/view_exam_center.html",context)


def update_exam_center(request, id):

    # Getting exam center based on Id
    exam_center = get_object_or_404(ExamCenter,id=id)

    if request.method == "POST":
        form = ExamCenterForm(request.POST,instance=exam_center)

        if form.is_valid():
            form.save()
            return redirect("view_exam_center")

    else:
        form = ExamCenterForm(instance=exam_center)

    context = { "form": form}

    return render(request,"exam_center/update_exam_center.html",context)


def delete_exam_center(request, id):

    exam_center = get_object_or_404(
        ExamCenter,
        id=id
    )

    exam_center.delete()

    return redirect(
        "view_exam_center"
    )

def home(request):
    
    return render( request, "exam_center/home.html")