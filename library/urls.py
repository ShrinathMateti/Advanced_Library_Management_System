from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('student_login/',views.student_login,name='student_login'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('student_registration/',views.student_registration,name='student_registration'),
    path('profile/',views.profile,name='profile'),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path('add_book/',views.add_book,name='add_book'),
    path('view_books/',views.view_books,name='view_books'),
    path('issue_book/',views.issue_book,name='issue_book'),
    path('view_issued_book/',views.view_issued_book,name='view_issued_book'),
    path("book_update/<int:id>",views.book_update,name="book_update"),
    path("delete_book/<int:myid>/", views.delete_book,name="delete_book"),
    path('view_students/',views.view_students,name='view_students'),
    path('student_issued_books/',views.student_issued_books,name='student_issued_books'),
    path('change_password/',views.change_password,name='change_password'),
    path("delete_student/<int:myid>/", views.delete_student,name="delete_student"),
    path("logout/", views.Logout, name="logout")    
]
