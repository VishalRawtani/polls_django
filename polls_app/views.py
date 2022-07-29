from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Polls


class PollsListView(ListView):
    model = Polls
    template_name = "home.html"


class PollsDetailView(DetailView):
    model = Polls
    template_name = "poll_detail.html"
    context_object_name = "poll"
