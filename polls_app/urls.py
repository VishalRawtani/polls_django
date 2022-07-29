from django.urls import path
from .views import PollsListView, PollsDetailView, PollsCreateView

urlpatterns = [
    path("poll/new", PollsCreateView.as_view(), name="poll_new"),
    path("poll/<int:pk>", PollsDetailView.as_view(), name="poll_detail"),
    path("", PollsListView.as_view(), name="home"),
]
