from django.urls import path
from basicapp import views
app_name="basicapp"

urlpatterns=[
path('',views.SchoolList.as_view(),name='list'),
path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),]
# list is a string we can use any name
