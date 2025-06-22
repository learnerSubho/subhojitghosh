from admin_corner import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',views.register,name='register'),
    path('to_login/', views.to_login, name='to_login'),
    path('logout/', views.user_logout, name='logout'),
    path('index/', views.index, name='index'),
    path("success/", views.success, name="success"),
    path('desc/', views.desc, name='desc'),
    path('delete_desc/',views.delete_desc,name='delete_desc'),
    path('frontImage/',views.frontImage,name='frontImage'),
    path('delete_frontImage/',views.delete_frontImage,name='delete_frontImage'),
    path('upload_cv/',views.upload_cv,name='upload_cv'),
    path('delete_cv/',views.delete_cv,name='delete_cv'),
    path('add_experiences/',views.add_experiences,name='add_experiences'),
    path('delete_experience/<int:experience_id>/',views.delete_experience,name='delete_experience'),
    path('add_projects/',views.add_projects,name='add_projects'),
    path('delete_project/<int:project_id>',views.delete_project,name='delete_project'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('delete_blog/<int:blog_id>',views.delete_blog,name='delete_blog'),
    # path('messages/',views.messages,name='messages'),
    path('view_project/<int:id>',views.view_project,name='view_project'),
    path('mark_as_seen/<int:message_id>/', views.mark_as_seen, name='mark_as_seen'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
