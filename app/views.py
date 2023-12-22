from django.shortcuts import render, get_object_or_404, redirect
from .models import Estimation, Subject, Student
from .forms import EstimationForm, SubjectForm, StudentForm


# Student
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_edit.html',
                  {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


# Estimation
def estimation_list(request):
    estimations = Estimation.objects.all()
    return render(request, 'estimation_list.html', {'estimations': estimations})


def add_estimation(request):
    if request.method == 'POST':
        form = EstimationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estimation_list')
    else:
        form = EstimationForm()
    return render(request, 'estimation_form.html', {'form': form})

def edit_estimation(request, pk):
    estimation = get_object_or_404(Estimation, pk=pk)
    if request.method == 'POST':
        form = EstimationForm(request.POST, instance=estimation)
        if form.is_valid():
            form.save()
            return redirect('estimation_list')
    else:
        form = EstimationForm(instance=estimation)
    return render(request, 'estimation_edit.html', {'form': form})


def delete_estimation(request, pk):
    estimation = get_object_or_404(Estimation, pk=pk)
    estimation.delete()
    return redirect('estimation_list')


# Subject

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})

def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subject_edit.html', {'form': form})

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subject_list')
