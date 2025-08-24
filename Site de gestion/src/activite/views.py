from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Activity, MemberUser, InfoOut


# Create your views here.
def signup(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        second_password = request.POST.get('password2')
        if password != second_password:
            return render(request, 'singup.html', {"error": True} )
        user=MemberUser.object.create_user(username=username, password=password)
        login(request, user=user)
        return render(request, 'created_account.html')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def index(request):
    return render(request,"index.html")

def community(request):
    return render(request,"community.html")

class ActivitiesView(ListView):

    model = Activity

    template_name = 'activities.html'

    context_object_name = 'activities'

class ActivityDetail(DetailView):

    model = Activity
    template_name = 'detail.html'

    context_object_name = "activity"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity = self.get_object()
        context['members'] = activity.member.all()
        return context



def quit_process(request):
    return render(request,"quit_process.html")

def out_community(request):
    user=MemberUser.object.get(pk=request.user.pk)
    user.in_community=False
    user.save()
    return redirect('activity:home')

class InfoOutCreateView(CreateView):
    model=InfoOut
    fields = ['reason']
    template_name = 'reason.html'

    def form_valid(self, form):
        form.instance.member=self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('activity:home')

class CommissionMembersView(ListView):

    model = MemberUser
    context_object_name = 'members'
    template_name = 'memberuser_list.html'
    def get_queryset(self):
        commission = self.kwargs.get('commission')
        queryset = MemberUser.object.filter(commission=commission)
        return queryset

def contact(request):
    return render(request, 'contact.html')

def created(request):
    return render(request, 'created_account.html')