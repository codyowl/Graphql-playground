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
	all_categories = graphene.List(BookType)
    all_ingredients = graphene.List(AuthorType)				
