from xml.etree.ElementTree import Comment
from django import forms
from .models import Book, Comment, Suggestion


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "url", "description", "pic"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ["title", "author", "url", "description", "pic"]
