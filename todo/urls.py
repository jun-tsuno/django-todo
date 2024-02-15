from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoView.as_view(), name='top-page'),
    path('todo/<int:pk>', views.TodoDetailView.as_view(), name='todo-detail-page'),
    path('todo/<int:pk>/update', views.TodoUpdateView.as_view(), name='update'),
    path('todo/<int:pk>/delete', views.TodoDeleteView.as_view(), name='delete'),
    path('create/', views.TodoCreateView.as_view(), name='create-todo-page')
]