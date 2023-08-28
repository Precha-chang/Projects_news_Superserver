from django.db import models

# Create your models here.

name_prefix_choice = (
    (1, 'นาย'),
    (2, 'นาง'),
    (3, 'นางสาว'),
)


class Author(models.Model):
    """Model definition for Author."""
    prefix = models.IntegerField(choices=name_prefix_choice)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return self.first_name + " "+self.last_name


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title