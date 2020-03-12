from django.urls import path
from . import views


urlpatterns=[
    path('',views.PostListView.as_view(),name='blogpost_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('blogpost/<int:pk>',views.PostDetailView.as_view(),name='blogpost_detail'),
    path('blogpost/new/',views.PostCreateView.as_view(),name='blogpost_new'),
    path('blogpost/<int:pk>/edit/',views.PostUpdateView.as_view(),name='blogpost_edit'),
    path('drafts/',views.PostDraftListView.as_view(),name='blogpost_draft_list'),
    path('blogpost/<int:pk>/remove/',views.PostDeleteView.as_view(),name='blogpost_remove'),
    path('blogpost/<int:pk>/publish/', views.post_publish, name='blogpost_publish'),
    path('blogpost/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),

]
