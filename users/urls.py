from os import name
from django.urls import path
from .views import (
    RegisterUser,
    LoginUser,
    UserDashboard,
    AllPosts,
    NewPost,
    EditPost,
    DeletePost,
    AllComments,
    EditComment,
    DeleteComment,
    UserProfile,
    DeleteUser,
    ChangePassword,
    LogoutUser
)


urlpatterns = [
    path('register/', LoginUser.as_view(), name='user_register'),
    path('login/', RegisterUser.as_view(), name='user_login'),
    path('user/', UserDashboard.as_view(), name='user_dashboard'),
    path('user/all-posts/', AllPosts.as_view(), name='user_all_posts'),
    path('user/new-post/', NewPost.as_view(), name='user_new_post'),
    path('user/edit-post/<str:slug>/', EditPost.as_view(), name='user_edit_post'),
    path('user/delete-post/<str:slug>/', DeletePost.as_view(), name='user_delete_post'),
    path('user/all-comments/', AllComments.as_view(), name='user_all_comments'),
    path('user/edit-comment/<int:pk>/', EditComment.as_view(), name='user_edit_comment'),
    path('user/delete-comment/<int:pk>/', DeleteComment.as_view(), name='user_delete_comment'),
    path('user/edit-profile/', UserProfile.as_view(), name='user_edit_profile'),
    path('user/delete-profile/', DeleteUser.as_view(), name='user_delete_profile'),
    path('user/change-password/', ChangePassword.as_view(), name='user_change_password'),
    path('user/logout/', LogoutUser.as_view(), name='user_logout')
]
