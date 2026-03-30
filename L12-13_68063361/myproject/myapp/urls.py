from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about),
    path('form/',views.form, name='form'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('delete/<int:id>/',views.delete, name='delete'),
]