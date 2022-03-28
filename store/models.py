from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField('Brand name', max_length=25)
    country = models.CharField('Made in country', max_length=25)
    note = models.TextField('Notes', blank=True, null=True, max_length=400)

    class Meta:
        verbose_name = 'Brand bike'
        verbose_name_plural = 'Brands bike'

    def __str__(self):
        return self.name


class BikeModel(models.Model):
    CATEGORY_BIKES = [
        ('MTB', 'Mountain'),
        ('EBike', 'Electric Bike'),
        ('Cross', 'Cross Bike'),
        ('Child', 'Child Bike'),
        ('Road', 'Road Bike'),
    ]
    name = models.CharField('Model name', max_length=40)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT)
    type = models.CharField('Types of bike', max_length=15, choices=CATEGORY_BIKES)

    class Meta:
        verbose_name = 'Model bike'
        verbose_name_plural = 'Models bike'

    def __str__(self):
        return self.name


class Post(models.Model):
    SIZE_FRAME = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    ]
    title = models.CharField('Title post', max_length=75)
    description = models.TextField('Description')
    model = models.ForeignKey('BikeModel', on_delete=models.PROTECT)
    size = models.CharField('Size frame', max_length=15, choices=SIZE_FRAME)
    pub_date = models.DateTimeField('Public date', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bike'
        verbose_name_plural = 'Bikes'

    def __str__(self):
        return self.title


class ImageBike(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    image = models.ImageField('Photo bike', upload_to='bike/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Photo bike'
        verbose_name_plural = 'Photo bikes'

    def __str__(self):
        return self.post
