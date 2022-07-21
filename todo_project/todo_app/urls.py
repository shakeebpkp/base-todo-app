from django.urls import path
from. import views
urlpatterns = [
   path('',views.index,name='index'),
   path('delete/<int:taskid>/',views.delete,name='delete'),
   path('upate/<int:id>/',views.update,name='update'),
   path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
   path('cbvdetail/<int:pk>/',views.TasklDetailview.as_view(),name='cbvdetail'),
   path('cbvupdate/<int:pk>/',views.TasklUpdateview.as_view(),name='cbvupdate'),
   path('cbvdelete/<int:pk>/',views.TasklDeleteview.as_view(),name='cbvdelete'),

]