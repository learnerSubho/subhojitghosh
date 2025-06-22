from django.shortcuts import render,redirect
from admin_corner import models
def portpholio(request):
    context = {'Subhojit':models.frontImage.objects.last(),
               'Subhojit_desc':models.description.objects.first(),
               'Subhojit_cv':models.CV.objects.first(),
               'Subhojit_experience':models.Timeline_Details.objects.all(),
               'Subhojit_projects':models.Projects.objects.all(),
               'Subhojit_blogs':models.Blog.objects.all(),
               }
    return render(request, 'portpholio.html',context)

def messages(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('msg')
        print(name, email, subject)
        models.Messages.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
    return redirect('portpholio')