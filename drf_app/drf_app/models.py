from django.db import models


CATEGORIES = (
    ("FICTION", "Fiction"),
    ("TECH", "Tech"),
    ("PSYCHOLOGY", "Psychology")
)


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.CharField(max_length=128)

    @property
    def author_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    category = models.CharField(max_length=15, choices=CATEGORIES, default="FICTION")

    def __str__(self) -> str:
        return self.category 


class Book(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.title 
