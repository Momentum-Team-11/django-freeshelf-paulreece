import csv
from http.client import CREATED
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Book, User, Comment
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BookForm, CommentForm, SuggestionForm
from django.db import models
from django.contrib.auth.views import LoginView


def homepage(request):
    if request.user.is_authenticated:
        return redirect("book_list")

    return render(request, "base.html")


@login_required(login_url="auth_login")
def book_list(request):
    # with open("sample_books.csv", "r") as file:
    #     reader = csv.reader(file)
    #     fields = next(reader)
    #     for row in reader:
    #         _, created = Book.objects.update_or_create(
    #             title=row[0],
    #             author=row[1],
    #             url=row[2],
    #             description=row[3],
    #             date=datetime.now(),
    #             pic="",
    #         )

    books = Book.objects.all().order_by("date")

    return render(request, "book_list.html", {"books": books})


def check_admin_user(user):
    return user.is_staff


@login_required(login_url="auth_login")
@user_passes_test(check_admin_user)
def list_books(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


@login_required(login_url="auth_login")
def asc_order(request):
    books = Book.objects.all().order_by("date")
    return render(request, "desc_order.html", {"books": books})


@login_required(login_url="auth_login")
def desc_order(request):
    books = Book.objects.all().order_by("-date")
    return render(request, "asc_order.html", {"books": books})


@login_required(login_url="auth_login")
def add_book(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user_id = pk
            book.save()
            return redirect(to="book_list")

    return render(request, "add_book.html", {"form": form, "user": user})


def show_category(request, slug):
    books = Book.objects.filter(category__slug=slug)
    return render(request, "book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.all()
    return render(request, "book_detail.html", {"book": book, "comments": comments})


def add_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "GET":
        favorite = Book

    else:
        now = datetime.datetime.now()
        numbered = book.favorited_number
        numbered += 1
        favorite = Book(request.method == "POST")

        Book.objects.filter(pk=book.pk).update(
            favorite="⭐", favorite_date=now, favorited_number=numbered
        ),

        return redirect(to="list_favorites")
    return render(
        request,
        "add_favorite.html",
        {
            "book": book,
            "favorite": favorite,
        },
    )


def remove_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        favorite = Book
    else:
        favorite = Book(request.method == "POST")
        Book.objects.filter(pk=book.pk).update(favorite="")
        return redirect(to="list_favorites")
    return render(request, "remove_favorite.html", {"book": book, "favorite": favorite})


@login_required(login_url="auth_login")
def list_favorites(request):
    books = Book.objects.filter(favorite="⭐").order_by("favorite_date")

    return render(request, "list_favorites.html", {"books": books})


def add_javascript(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        booky = Book

    else:
        booky = Book(request.method == "POST")
        book.category.add("1"),

        return redirect(to="book_list")
    return render(
        request,
        "add_js.html",
        {"book": book, "booky": booky},
    )


def add_python(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        booky = Book

    else:
        booky = Book(request.method == "POST")
        book.category.add("2"),

        return redirect(to="book_list")
    return render(
        request,
        "add_python.html",
        {"book": book, "booky": booky},
    )


def add_gaming(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        booky = Book

    else:
        booky = Book(request.method == "POST")
        book.category.add("3"),

        return redirect(to="book_list")
    return render(
        request,
        "add_gaming.html",
        {"book": book, "booky": booky},
    )


def add_testing(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        booky = Book

    else:
        booky = Book(request.method == "POST")
        book.category.add("4"),

        return redirect(to="book_list")
    return render(
        request,
        "add_testing.html",
        {"book": book, "booky": booky},
    )


def add_comment(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect(to="book_detail", pk=book.pk)

    return render(request, "add_comment.html", {"form": form, "book": book})


@login_required(login_url="auth_login")
def add_suggestion(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        form = SuggestionForm()
    else:
        form = SuggestionForm(data=request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user_id = pk
            suggestion.save()
            return redirect(to="book_list")

    return render(request, "add_suggestion.html", {"form": form, "user": user})


def user_comments(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.all()
    return render(request, "user_comments.html", {"book": book, "comments": comments})
