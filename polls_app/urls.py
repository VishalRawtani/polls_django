from django.urls import path
from .views import PollsListView, PollsDetailView

urlpatterns = [
    path("poll/<int:pk>", PollsDetailView.as_view(), name="poll_detail"),
    path("", PollsListView.as_view(), name="home"),
]
