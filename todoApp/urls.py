from django.urls import path

# import View dari todo Application
from .views import index_view, detail_view, create_view, update_view, delete_view

app_name = 'todoApp'
urlpatterns = [
    # route untuk halaman daftar tugas
    path('', index_view, name='index'),
    # route untuk halaman detail task
    path('detail/<int:task_id>', detail_view, name='detail'),
    # url untuk halaman tambah task
    path('create', create_view, name='create'),
    # url untuk halaman ubah task
    path('update/<int:task_id>', update_view, name='update'),
    # url untuk mengahapus task
    path('delete/<int:task_id>', delete_view, name='delete'),
]
