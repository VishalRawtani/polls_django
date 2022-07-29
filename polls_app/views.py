from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Polls


class PollsListView(ListView):
    model = Polls
    template_name = "home.html"


class PollsDetailView(DetailView):
    model = Polls
    template_name = "poll_detail.html"
    context_object_name = "poll"


class PollsCreateView(CreateView):
    model = Polls
    template_name = "polls_create.html"
    fields = ["owner", "question", "choice1", "choice2", "choice3", "choice4"]
