# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Book
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Purple(LoginRequiredMixin, TemplateView):
    template_name = "web/purple.html"
    
    
class Forms(TemplateView):
    template_name = "web/pages/forms/basic_elements.html"
    
    
class Icons(TemplateView):
    template_name = "web/pages/icons/mdi.html"
    
    
class Buttons(TemplateView):
    template_name = "web/pages/ui-features/buttons.html"
    
    
class Typography(TemplateView):
    template_name = "web/pages/ui-features/typography.html"
    
    
class Charts(TemplateView):
    template_name = "web/pages/charts/chartjs.html"
    
    
class Tables(TemplateView):
    template_name = "web/pages/tables/basic-table.html"
    
    
class Error(TemplateView):
    template_name = "web/pages/error-404.html"

class BookCreate(LoginRequiredMixin, CreateView):
    model=Book
    fields="__all__"
    template_name = "web/book_form.html"
    

class BookList(LoginRequiredMixin, ListView):
    model=Book
    fields="__all__"
    template_name = "web/book_list.html"
    # success_url = reverse_lazy('app:book_list')
    def get_success_url(self):
        return reverse_lazy('app:bookdetail', kwargs={'pk': self.pk})


class BookDetail(LoginRequiredMixin, DetailView):
    model =  Book
    template_name = "web/book_detail.html"
    fields = '_all_'


class BookUpdate(LoginRequiredMixin, UpdateView):
    model =  Book
    template_name = "web/book_update.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('app:booklist')


class BookDelete(LoginRequiredMixin, DeleteView):
    model =  Book
    template_name = "web/book_delete.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('app:booklist')