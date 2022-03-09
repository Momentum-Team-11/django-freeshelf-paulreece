"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as book_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path("", book_views.homepage, name="homepage"),
    path("books/", book_views.book_list, name="book_list"),
    path("books/<int:pk>/add/", book_views.add_book, name="add_book"),
    path("books/<int:pk>/detail", book_views.book_detail, name="book_detail"),
    path("books/asc", book_views.asc_order, name="sort_books_asc"),
    path("books/desc", book_views.desc_order, name="sort_books_desc"),
    path("books/<slug:slug>", book_views.show_category, name="show_category"),
    path("books/javascript", book_views.show_category, name="show_javascript"),
    path("books/python", book_views.show_category, name="show_python"),
    path("books/gaming", book_views.show_category, name="show_gaming"),
    path("books/testing", book_views.show_category, name="show_testing"),
    path("books/<int:pk>/favorite/", book_views.add_favorite, name="add_favorite"),
    path(
        "books/<int:pk>/remove_favorite/",
        book_views.remove_favorite,
        name="remove_favorite",
    ),
    path("favorites", book_views.list_favorites, name="list_favorites"),
    path("<int:pk>/suggestions", book_views.add_suggestion, name="add_suggestion"),
    path(
        "books/<int:pk>/javascript/", book_views.add_javascript, name="add_javascript"
    ),
    path("books/<int:pk>/python/", book_views.add_python, name="add_python"),
    path("books/<int:pk>/gaming/", book_views.add_gaming, name="add_gaming"),
    path("books/<int:pk>/testing/", book_views.add_testing, name="add_testing"),
    path("books/<int:pk>/comment", book_views.add_comment, name="add_comment"),
    path("comments", book_views.user_comments, name="user_comments"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
