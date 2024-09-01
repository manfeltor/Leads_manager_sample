from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FormSubmission, CustomUser, ESTADO_CHOICES
from .forms import FormSubmissionEditForm
from django.utils.dateparse import parse_date

@login_required
def forms_list_view(request):
    # Start with all forms
    forms = FormSubmission.objects.all()

    # Get filter parameters from the request
    assigned_user_id = request.GET.get('assigned_user')
    estado = request.GET.get('estado')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Filter by assigned user if provided
    if assigned_user_id:
        forms = forms.filter(assigned_user_id=assigned_user_id)

    # Filter by estado if provided
    if estado:
        forms = forms.filter(estado=estado)

    # Filter by date range if provided
    if start_date:
        forms = forms.filter(fecha_creacion__gte=start_date)
    if end_date:
        forms = forms.filter(fecha_creacion__lte=end_date)

    # Get all users and estados for the dropdowns
    users = CustomUser.objects.all()
    estados = FormSubmission._meta.get_field('estado').choices

    return render(request, 'list_forms_submissions.html', {
        'forms': forms,
        'users': users,
        'estados': estados,
    })

@login_required
def user_leads_view(request):
    user_leads = FormSubmission.objects.filter(assigned_user=request.user)

    # Get filter values from the request
    status_filter = request.GET.get('status')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    # Apply status filter if provided
    if status_filter:
        user_leads = user_leads.filter(estado=status_filter)

    # Apply date filters if provided
    if date_from:
        user_leads = user_leads.filter(fecha_creacion__date__gte=parse_date(date_from))
    if date_to:
        user_leads = user_leads.filter(fecha_creacion__date__lte=parse_date(date_to))

    context = {
        'user_leads': user_leads,
        'status_filter': status_filter,
        'date_from': date_from,
        'date_to': date_to,
        'estado_choices': ESTADO_CHOICES,  # Pass status choices to the template
    }

    return render(request, 'user_leads_list.html', context)

@login_required
def form_detail_view(request, submission_id):
    form = get_object_or_404(FormSubmission, submission_id=submission_id)
    return render(request, 'form_detail.html', {'form': form})

@login_required
def user_form_detail_view(request, submission_id):
    form = get_object_or_404(FormSubmission, submission_id=submission_id)
    return render(request, 'user_form_detail.html', {'form': form})

@login_required
def form_edit_view(request, submission_id):
    form_instance = get_object_or_404(FormSubmission, submission_id=submission_id)

    if not request.user.is_management:
        return redirect('unauthorized')

    if request.method == 'POST':
        form = FormSubmissionEditForm(request.POST, instance=form_instance)
        if form.is_valid():
            form.save(commit=False)
            form_instance.save(user=request.user)  # Pass the logged-in user
            return redirect('form_detail', submission_id=submission_id)
    else:
        form = FormSubmissionEditForm(instance=form_instance)

    return render(request, 'form_edit.html', {'form': form, 'form_instance': form_instance})

@login_required
def user_form_edit_view(request, submission_id):
    form_instance = get_object_or_404(FormSubmission, submission_id=submission_id)

    if request.method == 'POST':
        form = FormSubmissionEditForm(request.POST, instance=form_instance)
        if form.is_valid():
            new_status = form.cleaned_data['estado']

            # # Check if the status change is allowed for non-management users
            # if not form_instance.is_status_change_allowed(new_status, request.user):
            #     return redirect('status_change_not_allowed')  # Redirect to an error page if not allowed

            # Save the changes with the current user
            form_instance.save(user=request.user)
            return redirect('form_detail', submission_id=submission_id)
    else:
        form = FormSubmissionEditForm(instance=form_instance)

    return render(request, 'user_form_edit.html', {'form': form, 'form_instance': form_instance})

def status_change_not_allowed_view(request):
    return render(request, 'status_change_not_allowed.html')