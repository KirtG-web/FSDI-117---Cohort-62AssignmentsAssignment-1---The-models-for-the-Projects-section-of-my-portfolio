from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill
from .forms import ProjectForm, SkillForm, ContactForm


# --- existing views ---
def home(request):
    return render(request, 'portfolio/home.html')


def about(request):
    return render(request, 'portfolio/about.html')


def experience(request):
    return render(request, 'portfolio/experience.html')


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})


def skills(request):
    skills_list = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills_list})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'portfolio/add_project.html', {'form': form})


# --- add skill ---
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = SkillForm()

    return render(request, 'portfolio/add_skill.html', {'form': form})


# --- contact form view ---
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body = (
                f'You have a new email from your portfolio contact form.\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}'
            )
            try:
                send_mail(
                    "Email from portfolio contact form",
                    message_body,
                    settings.EMAIL_HOST_USER,  # use your Gmail account
                    [settings.EMAIL_HOST_USER],  # send to yourself
                )
                form = ContactForm()
                return render(request, 'portfolio/contact.html', {'form': form})
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'portfolio/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})