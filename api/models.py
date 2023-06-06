from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from autoslug import AutoSlugField


class Book(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='title', unique=True,always_update=True,default='x')

    def __str__(self) -> str:
        return self.title
    
class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # def __str__(self) -> str:
    #     return self.book.title

    class Meta:
        # unique_together = [['user', 'book'],]
        constraints = [
                models.UniqueConstraint(fields=['book','user'], name="book_user_rating"),
                ]
        # index_together = [['user', 'book'],]
        indexes = [
            models.Index(fields=['user', 'book']),
        ]
