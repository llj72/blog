from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    #글쓰기 목록 페이지
    path("", views.index, name='index'),

    #글쓰기 등록
    path('post_create/', views.post_create, name="post_create")
]