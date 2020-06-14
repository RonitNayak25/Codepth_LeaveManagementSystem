from django.shortcuts import render, redirect
from .forms import UserRegisterForm, StudentForm
from django.contrib import messages
from rest_framework.decorators import api_view
from .models import Leave
from .serializers import LeaveCreateSerializer, LeaveListSerializer, LeaveUpdateSerializer
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import generics


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can Login.')
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'MyApp/signup.html', context)


@login_required(login_url='login/')
def index(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'MyApp/home.html', context)


class LeaveCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Leave
    fields = ['start_date', 'end_date', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.user_type == 1:
            return True
        return False


class LeaveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Leave
    fields = ['is_accepted', 'comment']

    def test_func(self):
        if self.request.user.user_type == 2:
            return True
        return False


class LeaveListView(LoginRequiredMixin, ListView):
    model = Leave
    template_name = 'MyApp/leave_list.html'
    context_object_name = 'leaves'
    queryset = Leave.objects.all().order_by('id')


# Endpoints

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'All Leave Applications': 'http://127.0.0.1:8000/api/list/',
        'Create Leave Application': 'http://127.0.0.1:8000/api/create/',
        'Authorize LEave Application': 'http://127.0.0.1:8000/api/update/<int:pk>/',
    }

    return Response(api_urls)


class LeaveList(LoginRequiredMixin, generics.ListAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveListSerializer


class LeaveCreate(LoginRequiredMixin, UserPassesTestMixin, generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveCreateSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    def test_func(self):
        if self.request.user.user_type == 1:
            return True
        return False


class LeaveUpdate(LoginRequiredMixin, UserPassesTestMixin, generics.UpdateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

    def test_func(self):
        if self.request.user.user_type == 2:
            return True
        return False
