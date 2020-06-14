from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('leave/new/', LeaveCreateView.as_view(template_name='MyApp/leave_form.html'), name='create'),
    path('login/', LoginView.as_view(template_name='MyApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='MyApp/logout.html'), name='logout'),
    path('leave/<int:pk>/update', LeaveUpdateView.as_view(), name='leave_update'),
    path('leave_list', LeaveListView.as_view(), name='leave_list'),
    path('api/', api_overview, name='endpoints'),
    path('api/list/', LeaveList.as_view(), name='endpoint-list'),
    path('api/create/', LeaveCreate.as_view(), name='endpoint-create'),
    path('api/update/<int:pk>/', LeaveUpdate.as_view(), name='endpoint-update'),
]
