from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Registration Successfull')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'TodoListreg/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Information Updated!')
            return redirect('profile')
    else:
        u_form = UpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'TodoListreg/profile.html', context)