from django.urls import  path
from Blog import views as Blogsview
from . import views

urlpatterns = [
    path('users/register/', views.register, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('users/editor/dashboard/', views.editor_dashboard, name='editor_dashboard'),
    path('users/author/dashboard/', views.author_dashboard, name='author_dashboard'),

    #posts CRUD
    path('users/posts/', Blogsview.posts_list, name='posts_list'),
    path('users/posts/create/', Blogsview.post_create, name='post_create'),
    path('users/posts/<int:pk>/edit/', Blogsview.post_update, name='post_update'),
    path('users/posts/<int:pk>/delete/', Blogsview.post_delete, name='post_delete'),

    #categories CRUD
    path("users/categories/", Blogsview.category_list, name="category_list"),
    path("users/categories/add/", Blogsview.category_create, name="category_create"),
    path("users/categories/edit/<int:pk>/", Blogsview.category_update, name="category_update"),
    path("users/categories/delete/<int:pk>/", Blogsview.category_delete, name="category_delete"),

    #users CRUD
    path('users/', Blogsview.users_list, name='users_list'),
    path('users/create/', Blogsview.user_create, name='user_create'),
    path('users/<int:pk>/edit/', Blogsview.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', Blogsview.user_delete, name='user_delete'),
    path('users/<int:pk>/toggle/', Blogsview.toggle_user_active, name='toggle_user_active'),  # Activate/Deactivate

    #system_reports
    path("users/reports/", Blogsview.system_reports, name="system_reports"),

    #role request
    path("request-author/", views.request_author_role, name="request_author_role"),
    path("role-requests/", views.manage_role_requests, name="manage_role_requests"),
    path("role-requests/<int:pk>/approve/", views.approve_role_request, name="approve_role_request"),
    path("role-requests/<int:pk>/reject/", views.reject_role_request, name="reject_role_request"),
]