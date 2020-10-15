from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import List
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': List.objects.all()
    }
    return render(request, 'TodoList/home.html',context)


class ListView(ListView):
    model = List
    template_name = 'TodoList/home.html'
    context_object_name = 'lists'
    ordering = ['-date_posted']


class ListDetailView(DetailView):
    model = List


class ListCreateView(LoginRequiredMixin,CreateView):
    model = List
    fields = ['ListName', 'content', ]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = List
    fields = ['ListName', 'content', ]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        list = self.get_object()
        if self.request.user == list.author:
            return True
        return False   
    

class ListDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = List   
    success_url = '/'

    def test_func(self):
        list = self.get_object()
        if self.request.user == list.author:
            return True
        return False    
    

