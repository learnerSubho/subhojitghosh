from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from public.models import Visitor
from public.utils import get_client_ip

def to_login(request):
    logo = models.frontImage.objects.last()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # or any admin page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html',{'logo':logo})

def user_logout(request):
    logout(request)
    return redirect('to_login')

@login_required
def success(request):
    return render(request, 'success.html')
@login_required
def index(request):
    current_desc = models.description.objects.first()
    current_img = models.frontImage.objects.last()
    filename = None
    if models.CV.objects.exists():
        filename = models.CV.objects.first().filename()
    experiences = models.Timeline_Details.objects.all()
    unseen = models.Messages.objects.filter(seen=False).count()
    
    ip = get_client_ip(request)

    visitor, created = Visitor.objects.get_or_create(ip_address=ip)
    if not created:
        visitor.visit_count += 1
        visitor.save()

    total_visits = sum(v.visit_count for v in Visitor.objects.all())
    unique_visits = Visitor.objects.count()
    
    context={
        'current_desc': current_desc,
        'current_img': current_img,
        'current_cv': models.CV.objects.first(),
        'filename': filename,
        'experiences': experiences,
        'projects': models.Projects.objects.all(),
        'my_blogs': models.Blog.objects.all(),
        'all_messages': models.Messages.objects.all().order_by('-date'),
        'unseen': unseen,
        'total_visits': total_visits,
        'unique_visits': unique_visits,
    }
    return render(request, 'index.html',context)
@login_required
def desc(request):
    if request.method == 'POST':
        content = request.POST.get('desc')
        if content:
            models.description.objects.all().delete()
            models.description.objects.create(content=content)
    current_desc = models.description.objects.first()
    return redirect('success')
@login_required
def delete_desc(request):
    models.description.objects.all().delete()
    return redirect('index')

@login_required
def frontImage(request):
    if request.method == 'POST':
        image = request.FILES.get('frontimage')
        if image:
            models.frontImage.objects.create(photo=image)

    latest_image = models.frontImage.objects.last()
    return redirect('success')
@login_required
def delete_frontImage(request):
    models.frontImage.objects.last().delete()
    return redirect('index')
@login_required
def upload_cv(request):
    if request.method == 'POST':
        document = request.FILES.get('cv_file')
        if document:
            models.CV.objects.all().delete()
            models.CV.objects.create(document=document)
    return redirect('success')
@login_required
def delete_cv(request):
    models.CV.objects.all().delete()
    return redirect('upload_cv')

@login_required
def add_experiences(request):
    if request.method == 'POST':
        company_name = request.POST.get('company')
        subject = request.POST.get('subject')
        timeline = request.POST.get('timeline')
        desc = request.POST.get('desc')
        
        models.Timeline_Details.objects.create(
            company_name = company_name,
            subject = subject,
            timeline = timeline,
            desc = desc
        )
    return redirect('success')
@login_required
def delete_experience(request, experience_id):
    try:
        experience = models.Timeline_Details.objects.get(id=experience_id)
        experience.delete()
    except models.Timeline_Details.DoesNotExist:
        pass
    return redirect('add_experiences')
@login_required
def add_projects(request):
    if request.method == 'POST':
        title = request.POST.get('project_name')
        desc = request.POST.get('project_desc')
        link = request.POST.get('project_link')
        image = request.FILES.get('project_image')
        video = request.FILES.get('project_video')
        if image:
            models.Projects.objects.create(
                title=title,
                desc=desc,
                link=link,
                image=image,
                video=video
            )
        else:
            models.Project_Details.objects.create(
            project_name=title,
            project_desc=desc,
            project_link=link
        )
    return redirect('success')
@login_required
def delete_project(request, project_id):
    try:
        project = models.Projects.objects.get(id=project_id)
        project.delete()
    except models.Projects.DoesNotExist:
        pass
    return redirect('add_projects')
@login_required
def add_blog(request):
    if request.method == 'POST':
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        if headline:
            models.Blog.objects.create(
                headline=headline,
                body=body
            )
        elif models.Blog.objects.last() and body:
            prev_body = models.Blog.objects.last().body
            prev_body+=body
        else:
            models.Blog.objects.create(
                body=body
            )
    return redirect('success')
@login_required
def delete_blog(request, blog_id):
    try:
        blog = models.Blog.objects.get(id=blog_id)
        blog.delete()
    except models.Blog.DoesNotExist:
        pass
    return redirect('add_blog')

@login_required
def view_project(request,id):
    projects = models.Projects.objects.get(id=id)
    context = {
        'projects': projects
    }
    return render(request, 'view.html', {'projects': projects})
@login_required
def register(request):
    return render(request, 'register.html')

@login_required
def mark_as_seen(request, message_id):
    try:
        message = models.Messages.objects.get(id=message_id)
        message.mark_as_seen()
    except models.Messages.DoesNotExist:
        pass
    return redirect('index')