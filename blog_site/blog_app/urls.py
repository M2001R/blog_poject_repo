from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:pk>/', views.details.as_view(), name='post_details'),
    path('create_post/', views.Post_create.as_view(), name="post_create" ),
    path('<int:pk>/update/', views.post_update.as_view(), name="post_update" ),
    path('<int:pk>/delete/', views.post_delete.as_view(), name="post_delete" ),

]