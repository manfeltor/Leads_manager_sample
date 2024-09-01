from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from formsapp.models import FormSubmission

def base(req):

    total_submissions = FormSubmission.objects.count()
    pending_submissions = FormSubmission.objects.filter(estado='pendiente').count()
    contacted_submissions = FormSubmission.objects.filter(estado__in=['faltaCotizar', 'cotizado']).count()
    active_submissions = FormSubmission.objects.filter(estado__in=['gestionExitosa', 'pospuesto', 'interezadoAvanzar']).count()
    recent_submissions = FormSubmission.objects.exclude(estado='negativo').order_by('-fecha_creacion')[:5]
    context = {
        'total_submissions': total_submissions,
        'pending_submissions': pending_submissions,
        'contacted_submissions': contacted_submissions,
        'active_submissions': active_submissions,
        'recent_submissions': recent_submissions,
    }
    
    return render(req, "landing.html", context=context)

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect URL after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'custom_login.html')