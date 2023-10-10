from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:board_id>/', views.board_detail, name="detail"),
    path('write/', views.board_write, name="write"),
    path('<int:board_id>/edit/', views.board_edit, name="edit"),
    path('<int:board_id>/del/', views.board_delete, name='delete')
    #     path('', views.board_list, name='index'),
    #     path('<int:board_id>/',
    #          views.board_detail,
    #          name="board_detail"),
    #     path('comments/',
    #          views.comment_list,
    #          name="comment_list"),
]