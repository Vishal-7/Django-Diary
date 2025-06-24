from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
# Create your views here.

from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "content"]

    def get_success_url(self):
        entry_id = self.kwargs['pk']
        return reverse_lazy(
            "entry-detail",
            kwargs={'pk': entry_id}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")