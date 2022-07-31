from django.urls import path
from .views import (
    PollsListView,
    PollsDetailView,
    PollsCreateView,
    ResultView,
    vote_view,
)

urlpatterns = [
    path("poll/vote/<poll_id>", vote_view, name="vote"),
    path("poll/result/<int:pk>", ResultView.as_view(), name="result"),
    path("poll/new", PollsCreateView.as_view(), name="poll_new"),
    path("poll/<int:pk>", PollsDetailView.as_view(), name="poll_detail"),
    path("", PollsListView.as_view(), name="home"),
]
