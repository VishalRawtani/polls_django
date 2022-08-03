from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Polls


class PollsListView(ListView):
    model = Polls
    template_name = "home.html"
    ordering = "-id"
    paginate_by = 10


class PollsDetailView(DetailView):
    model = Polls
    template_name = "poll_detail.html"
    context_object_name = "poll"


class ResultView(DetailView):
    model = Polls
    template_name = "result.html"
    context_object_name = "poll"


class PollsCreateView(LoginRequiredMixin, CreateView):
    model = Polls
    template_name = "polls_create.html"
    fields = ["question", "choice1", "choice2", "choice3"]

    def form_valid(self, form):
        # Setting owner to currently logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


@login_required
def vote_view(request, poll_id):
    poll = Polls.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST["optionsRadios"]
        if selected_option == "option1":
            poll.choice1_count += 1
        elif selected_option == "option2":
            poll.choice2_count += 1
        elif selected_option == "option3":
            poll.choice3_count += 1
        else:
            return HttpResponse(400, "Invalid form")

        poll.save()
        return redirect("result", poll_id)
    context = {"poll": poll}
    return render(request, "vote.html", context)


class MyPollsListView(LoginRequiredMixin, ListView):
    model = Polls
    template_name = "my_polls.html"
    ordering = "-id"

    def get_queryset(self):
        # Querying foreign key table username attribute
        poll = Polls.objects.filter(owner__username=self.request.user)
        return poll
