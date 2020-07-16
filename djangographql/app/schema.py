import graphene
from graphene_django.types import DjangoObjectType
from app.models import Book, Author

class BookType(DjangoObjectType):
	class Meta:
		model = Book


class AuthorType(DjangoObjectType):
	class Meta:
		model = Author


class Query(object):
	all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)	

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_all_authors(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Author.objects.select_related('book').all()
			
